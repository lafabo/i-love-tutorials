"""
This script gets info from GiantBomb via api,
research.stlouisfed.org/fred2/ via text parsing

And make with them adjusted "today" price of
old game gadgets and sexy plots with mathplot
"""

from __future__ import print_function
import argparse
import logging
import os
import tablib
import matplotlib.pyplot as plt
import numpy as np
from requests import get

CPI_DATA_URL = 'http://research.stlouisfed.org/fred2/data/CPIAUCSL.txt'


class CPIData(object):
    """Abstraction of the CPI data provided by FRED"""

    def __init__(self):
        # Each year will end up as simple key-val pair dict
        self.year_cpi = {}

        #
        self.last_year = None
        self.first_year = None

    def load_from_url(self, url, save_as=None):
        """Loads data from :param url
        Downloaded file can also be :param save_as into a location"""

        fp = get(url, stream=True, headers={'Accept-Encoding': None})

        if save_as is None:
            return self.load_from_file(fp.raw)

        else:
            with open(save_as, 'wb+') as out:
                while True:
                    buffer = fp.read(81920)
                    if not buffer:
                        break
                    out.write(buffer)
            with open(save_as) as fp:
                return self.load_from_file(fp)


    def load_from_file(self, fp):
        """Loads CPI data from a given file-like object."""
        # When iterating over the data file we will need a handful of temporary
        # variables:
        reached_dataset = False
        current_year = None
        year_cpi = []
        for line in fp:
            # The actual content of the file starts with a header line
            # starting with the string "DATE ". Until we reach this line
            # we can skip ahead.
            if not reached_dataset:
                if line.startswith("DATE "):
                    reached_dataset = True
                continue
            # Each line ends with a new-line character which we strip here
            # to make the data easier usable.
            data = line.rstrip().split()

            # While we are dealing with calendar data the format is simple
            # enough that we don't really need a full date-parser. All we
            # want is the year which can be extracted by simple string
            # splitting:
            year = int(data[0].split("-")[0])
            cpi = float(data[1])

            if self.first_year is None:
                self.first_year = year
            self.last_year = year

            # The moment we reach a new year, we have to reset the CPI data
            # and calculate the average CPI of the current_year.
            if current_year != year:
                if current_year is not None:
                    self.year_cpi[current_year] = sum(year_cpi) / len(year_cpi)
                year_cpi = []
                current_year = year
            year_cpi.append(cpi)

        # We have to do the calculation once again for the last year in the
        # dataset.
        if current_year is not None and current_year not in self.year_cpi:
            self.year_cpi[current_year] = sum(year_cpi) / len(year_cpi)


    def get_adjusted_price(self, price, year, current_year=None):
        """Returns the adjusted price from given year compared
        to what current year has been specified"""

        if current_year is None or current_year > 2016:
            current_year = 2015

        if year < self.first_year:
            year = self.first_year
        elif year > self.last_year:
            year = self.last_year

        year_cpi = self.year_cpi[year]
        current_cpi = self.year_cpi[current_year]

        return float(price) / year_cpi * current_cpi


class GiantBombAPI(object):
    """Using GiantBomb API to GET platforms call as generator"""

    base_url = 'http://www.giantbomb.com/api'

    def __init__(self, api_key):
        self.api_key = api_key

    def get_platforms(self, sort=None, filter=None, field_list=None):
        """Generators yielding platforms matching the given criteria"""

        # API allows to filter and sort data
        params = {}
        # Here we making some filters if it's needed
        if sort is not None:
            params['sort'] = sort
        if field_list is not None:
            params['field_list'] = ','.join(field_list)
        if filter is not None:
            params['filter'] = filter
            parsed_filters = []
            for key, val in filter.interitems():
                parsed_filters.append('{0}{1}'.format(key, val))
            params['filter'] = ','.join(parsed_filters)

        # Appending API Key and tell API we wanna get data as JSON
        params['api_key'] = self.api_key
        params['format'] = 'json'

        incomplete_result = True
        num_total_results = None
        num_fetched_results = 0
        counter = 0

        while incomplete_result:
            # GiantBomb api limit is only 100 items but
            # we can skip a certain nymber of items
            params['offset'] = num_fetched_results
            result = get(self.base_url + '/platforms/', params=params)

            result = result.json()

            if num_total_results is None:
                num_total_results = int(result['number_of_total_results'])

            num_fetched_results += int(result['number_of_page_results'])
            if num_fetched_results >= num_total_results:
                # stop the cycle
                incomplete_result = False

            for item in result['results']:
                logging.debug("Yielding platforms {} of {}".format(counter+1, num_total_results))

                # converting values into more useful format where appropriate
                if 'original_price' in item and item['original_price']:
                    item['original_price'] = float(item['original_price'])

                # making this generator
                yield item
                counter += 1


def is_valid_dataset(platform):
    """filtering our datasetes that we can't use
    since they are either lacking a release date or
    an original price. For rendering output we also
    need the name and platform"""
    if 'release_date' not in platform or not platform['release_date']:
        logging.warn(u"{0} has no release data".format(platform['name']))
        return False
    if 'original_price' not in platform or not platform['original_price']:
        logging.warn(u"{0} has no original price".format(platform['name']))
        return False
    if 'name' not in platform or not platform['name']:
        logging.warn(u"No platform name found for given dataset")
        return False
    if 'abbreviation' not in platform or not platform['abbreviation']:
        logging.warn(u"{0} has no abbreviation".format(platform['name']))
        return False
    return True


def generate_plot(platforms, output_file):
    """Generates a bar chart of the given platforms and writes in PNG file"""

    # Converting platforms in a labels
    labels = []
    values = []
    for platform in platforms:
        name = platform['name']
        adapted_price = platform['adjusted_price']
        price = platform['original_price']

        if price > 2000:
            continue

        # if the name of platform too long replace it with abbrev
        if len(name) > 15:
            name = platform['abbreviation']
        labels.insert(0, u"{0}\n {1}\n {2}".format(name, price, round(adapted_price, 2)))
        values.insert(0, adapted_price)

    # let's define the width of each bar and graph size
    width = 0.3
    ind = np.arange(len(values))
    fig = plt.figure(figsize=(len(labels) * 1.8, 10))

    # generate subplot and put values into it
    ax = fig.add_subplot(1, 1, 1)
    ax.bar(ind, values, width, align='center')

    # format the x and y axis labels
    plt.ylabel('Adjusted price')
    plt.xlabel('Year/Console')
    ax.set_xticks(ind + 0.3)
    ax.set_xticklabels(labels)
    fig.autofmt_xdate()
    plt.grid(True)

    plt.savefig(output_file, dpi=72)


def generate_csv(platforms, output_file):
    """Writes the given platforms into a CSV output file"""

    dataset = tablib.Dataset(headers=['Abbreviation', 'Name', 'Year', 'Price', 'Adjusted price'])

    for p in platforms:
        dataset.append(p['abbreviation'], p['name'], p['year'], p['original_price'], p['adjusted_price'])

    if isinstance(output_file, basestring):
        with open(output_file, 'w+') as fp:
            fp.write(dataset.csv)
    else:
        output_file.write(dataset.csv)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--giantbomb-api-key', required=True, help="API key by GiantBomb.com")
    parser.add_argument('--cpi-file', default=os.path.join(os.path.dirname(__file__), 'CPIAUCSL.txt'),
                        help='Path to the file with CPI data (also target file if data has to be downloaded')
    parser.add_argument('--cpi-data-url', default=CPI_DATA_URL, help="URL to CPI data source")
    parser.add_argument('--debug', default=False, action='store_true', help='Increases the output level')
    parser.add_argument('--csv-file', help='Path to output CSV')
    parser.add_argument('--plot-file', help='Path to plot PNG')
    parser.add_argument('--limit', type=int, help='Number of recent platforms to be considered')

    opts = parser.parse_args()
    if not (opts.plot_file or opts.csv_file):
        parser.error('Specify --csv-file or --plot-file')
    return opts



def main():
    """This function handles the actual logic of this script."""
    opts = parse_args()

    if opts.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    cpi_data = CPIData()
    gb_api = GiantBombAPI(opts.giantbomb_api_key)

    print ("Disclaimer: This script uses data provided by FRED, Federal"
           " Reserve Economic Data, from the Federal Reserve Bank of St. Louis"
           " and Giantbomb.com:\n- {0}\n- http://www.giantbomb.com/api/\n"
           .format(CPI_DATA_URL))

    if os.path.exists(opts.cpi_file):
        with open(opts.cpi_file) as fp:
            cpi_data.load_from_file(fp)
    else:
        cpi_data.load_from_url(opts.cpi_data_url, save_as=opts.cpi_file)

    platforms = []
    counter = 0

    # Now that we have everything in place, fetch the platforms and calculate
    # their current price in relation to the CPI value.
    for platform in gb_api.get_platforms(sort='release_date:desc',
                                         field_list=['release_date',
                                                     'original_price', 'name',
                                                     'abbreviation']):
        # Some platforms don't have a release date or price yet. These we have
        # to skip.
        if not is_valid_dataset(platform):
            continue

        year = int(platform['release_date'].split('-')[0])
        price = platform['original_price']
        adjusted_price = cpi_data.get_adjusted_price(price, year)
        platform['year'] = year
        platform['original_price'] = price
        platform['adjusted_price'] = adjusted_price
        platforms.append(platform)

        # We limit the resultset on this end since we can only here check
        # if the dataset actually contains all the data we need and therefor
        # can't filter on the API level.
        if opts.limit is not None and counter + 1 >= opts.limit:
            break
        counter += 1

    if opts.plot_file:
        generate_plot(platforms, opts.plot_file)
    if opts.csv_file:
        generate_csv(platforms, opts.csv_file)


if __name__ == '__main__':
    main()
