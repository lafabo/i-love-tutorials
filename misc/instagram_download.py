#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import urllib
import time
import sys


def load_instagram(url):
	html = urllib2.urlopen(url).read()
	return str(html)


def get_image_url(page_source):
	before = '<meta property=\"og:image\" content=\"'
	pos = str(page_source).find(before)
	pos += 35
	image_link = ''
	while page_source[pos] != '\"':
		image_link += page_source[pos]
		pos += 1
	return image_link


def download_img(imgsource):
	filename = str(time.time()) + '.jpg'
	urllib.urlretrieve(imgsource, filename)
	return 'Saved as %s' % filename

if __name__ == '__main__':
	url = str(sys.argv[1])
	print download_img(get_image_url(load_instagram(url)))
