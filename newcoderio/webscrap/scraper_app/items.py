from scrapy.item import Item, Field


class LivingSocialDeal(item):
	"""Living social container (dictionary-like obj) for scraped data"""

	# all we need is Field()'s
	title, link, location, original_price, price, end_date = Field()

	