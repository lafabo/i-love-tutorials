#! /usr/bin/env python
#  -*- coding: utf-8 -*-
'''
this code uses urllib/2 to parse google translate, no api
'''

import urllib2, sys

#simple setting: user agent, google translate link, place in html
agents = {'User-Agent':"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}
before_trans = 'class="t0">'

def run():
	if len(sys.argv) == 4:
		# sys.argv[0] - is script's filename, as i know now
		fromlang = sys.argv[1]
		tolang = sys.argv[2]
		translate_str = sys.argv[3]
		print translate(translate_str, fromlang, tolang)          # <--- here is the start

	else:
		print 'You should run this with args like "$ script.py en ru "hello"'
		exit(1)

def translate(translate_str, fromlang, tolang):
	link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s" % (tolang, fromlang, translate_str.replace(" ", "+"))
	request = urllib2.Request(link, headers=agents)
	page = urllib2.urlopen(request).read()
	result = page[page.find(before_trans)+len(before_trans):]
	result = result.split("<")[0]
	return result

if __name__ == '__main__':
	run()

# TODO: This returns only one defenition per word!
	# Change all with https://pypi.python.org/pypi/goslate
	# especially use "Lookup Details in Dictionary" - section
