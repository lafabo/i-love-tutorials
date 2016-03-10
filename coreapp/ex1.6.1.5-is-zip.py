#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

if __name__ == '__main__':
	pattern = '(([0-9]{5})|([0-9]{4})) +(\w.+?).+'
	phrases = """
	1180 Bordeaux Drive
	3120 De La Cruz Boulevard
	3$ Coffee
	12 little ngrs
	"""
	print re.findall(pattern, phrases)


# here it works -> http://regexr.com/
# that's stragne