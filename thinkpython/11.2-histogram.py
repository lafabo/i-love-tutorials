#!/usr/bin/env python
# -*- coding: utf-8 -*-

lst = []
for i in open('words.txt'):
	lst.extend(list(i.strip('\r\n')))


def count_letters(lst):
	d = dict()
	for c in lst:
		d[c] = d.get(c, 0) + 1
	return d


def most_common(dict):
	for v in reversed(sorted(dict.values())):
		for key in dict:
			if dict[key] == v:
				print key, v
				break


most_common(count_letters(lst))