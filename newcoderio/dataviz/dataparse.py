import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import csv

my_file = 'data.csv'
delimiter = ','


def parse(raw_file, delimiter):
	"""Parse CSV file to JSON-line obj"""

	# Open CSV file
	opened_file = open(raw_file, 'r')
	# Read CSV
	csv_data = csv.reader(opened_file, delimiter=delimiter)

	# Build a data structure to return parsed_data
	# skip the first line (and i really don't know why we
	# need this .next() and not a range in csv_data[1:]
	parser_data = []
	fields = csv_data.next()
	for row in csv_data:
		parser_data.append(dict(zip(fields, row)))

	opened_file.close()

	return parser_data


def visualize_days():
	"""visualize data by day of a week"""

	# grab parsed data, count how many incidents
	data_file = parse(my_file, delimiter)
	counter = Counter(item['DayOfWeek'] for item in data_file)

	# separate x-axis data (days) from the counter
	# from the y-axis (number of incidents)
	data_list = [
		counter['Monday'],
		counter['Tuesday'],
		counter['Wednesday'],
		counter['Thursday'],
		counter['Friday'],
		counter['Saturday'],
		counter['Sunday'],
	]

	day_tulp = tuple(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])

	# y-axis data - > matplotlib plot instance
	plt.plot(data_list)
	# create the amount of ticks needed for our x-axis and assign the labels
	plt.xticks(range(len(day_tulp)), day_tulp)

	# save and close
	plt.savefig("Days.png")
	plt.clf()


def visualize_type():
	"""visualise data by category"""

	# grab parsed data, var Counter for incidents in categories
	data_file = parse(my_file, delimiter)
	counter = Counter(item['Category'] for item in data_file)

	# Set the labels based on counter.keys() because order doesn't matter
	labels = tuple(counter.keys())
	xlocations = np.arange(len(labels)) + 0.5

	# width of each  bar
	width = 0.5

	# Assign data to a bar plot, Assign labels and locations
	plt.bar(xlocations, counter.values(), width=width)
	plt.xticks(xlocations + width / 2, labels, rotation=-90)

	# Give some more room the x-axis
	plt.subplots_adjust(bottom=0.4)

	# Make the overall graph/figure larger
	plt.rcParams['figure.figsize'] = 12, 8

	# Save graph and close plot
	plt.savefig("Type.png")
	plt.close()




def main():
	# call our visualisation from parsed function and give it needed parameters
	visualize_days()
	visualize_type()


if __name__ == '__main__':
	main()