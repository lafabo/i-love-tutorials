#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
d = {}

for l in codecs.open('wiki_freq.txt', 'r', 'utf-8-sig'):
	w, f = l.split()
	if '-' in w:
		continue
	d[w] = int(f)

def longest(dic):
	longest = [sorted(d.keys(), key=lambda w:(len(w), d[w]), reverse=True)[:100]]
	return longest

def palindroms(dic):
	palindroms = sorted([w for w in d.keys() if w == w[-1::-1]],
	                    key = lambda  w:(len(w), d[w]), reversed=True)[:100]


if __name__ == '__main__':
	print(longest(d))
	print('\n\n\n')
	print(palindroms(d))