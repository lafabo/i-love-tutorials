#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
from collections import defaultdict
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
	return palindroms


def anagrams(dic):
	anagr= defaultdict(list)
	res = []
	for k in dic:
		if d[k] > 20:
			anagr[''.join(sorted(k))].append(k)
	for l in sorted(anagr.values(), key=len, reverse=True)[:10]:
		res.append(l)
	return res

if __name__ == '__main__':
	print(longest(d))
	print('\n\n\n')
	print(palindroms(d))
	print('\n\n\n')
	print(anagrams(d))