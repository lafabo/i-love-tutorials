#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import choice

lst = []
for i in open('words.txt'):
	lst.extend(list(i.strip('\r\n')))


def count_letters(lst):
	d = dict()
	for c in lst:
		d[c] = d.get(c, 0) + 1
	return d


def most_common(dict):
	result = {}
	for v in reversed(sorted(dict.values())):
		for key in dict:
			if dict[key] == v:
				result[key] = [v]

	return result


def select_from_hist(dict):
	res = []
	for word, frequency in dict.iteritems():
		print word, frequency
		res.extend([word] * frequency)

	return choice(res)


print select_from_hist(most_common(count_letters(lst)))