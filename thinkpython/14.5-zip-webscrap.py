#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import lxml.html


def get_args():
	try:
		zipcode = ''
		while len(str(zipcode)) != 5 and type(zipcode) != int:
			zipcode = int(raw_input("Enter your zip: "))

		return zipcode

	except ValueError:
		print 'Bad zipcode'


def get_url(zipcode):
	url = 'http://www.uszip.com/zip/%s' % zipcode
	page = urllib2.urlopen(url)
	return page


def get_zip_name(page):
	data = page.read()

	name = lxml.html.document_fromstring(data).xpath('//*[@id="content-body"]/div/div[2]/hgroup/h2/strong/text()')[0].strip()
	return name[:len(name)-1]   # i don't like the comma at the end


def get_zip_population(page):
	data = page.read()

	population = lxml.html.document_fromstring(data).xpath('//*[@id="content-body"]/div/div[2]/dl/dd[1]/text()')
	return population

# go
if __name__ == '__main__':
	url = get_url(get_args())
	print get_zip_name(url)
	# todo i don't know why zip_population gives an error
	# print get_zip_population(url)

