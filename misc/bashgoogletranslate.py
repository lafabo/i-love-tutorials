#! /usr/bin/env python
#  -*- coding: utf-8 -*-
'''
this code uses urllib/2 to parse google translate, no api

via http://habrahabr.ru/post/113243/
'''


import sys, re, urllib, urllib2, json

def print_params(data):
	'''print parameters to the data'''
	for val in data:
		if isinstance(val, basestring):
			print '\t' + val


def main():
	'''
	first arg - string to translate
	second arg - from lang
	third arg - to lang

	'hello' en ru
	:return:
	'''
	url = 'http://translate.google.com/translate_a/t?%s'
	list_of_params = {'client':'t', 'hl': 'en', 'multires':'1'}
	if len(sys.argv) == 4:
		list_of_params.update({'text': sys.argv[1], 'sl': sys.argv[2], 't': sys.argv[3]})
		request = urllib2.Request(url % urllib.urlencode(list_of_params),
		            headers={'User-Agent':'Mozilla/5.0', 'Accept-Charset': 'utf-8'})
		res = urllib2.urlopen(request).read()
		fixed_json = re.sub(r', {2, }', ',', res).replace(',]', ']')
		data = json.loads(fixed_json)

		print '%s / %s / %s' % (data[0][0][0], data[0][0][1], data[0][0][2] or data[0][0][3])

		if not isinstance(data[1], basestring):
			print data[1][0][0]
			print_params(data[1][0][1])

		try:
			if not isinstance(data[1][1], basestring):
				print data[1][1]
				print_params(data[1][0][1])
		except Exception:
			print 'no interjection'

	else:
		print main.__doc__

if __name__ == '__main__':
	main()