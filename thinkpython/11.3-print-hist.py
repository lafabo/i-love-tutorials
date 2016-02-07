#!/usr/bin/env python
# -*- coding: utf-8 -*-

lst = []
for i in open('words.txt'):
	lst.extend(list(i.strip('\r\n')))


def hist(lst):
	d = dict()
	for c in lst:
		d[c] = d.get(c, 0) + 1
	return d


def print_hist(dict):
	for key in dict:
		print key, dict[key]


print_hist(hist(lst))