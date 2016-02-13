#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import choice


lst = []
for i in open('words.txt'):
	lst.extend(list(i.strip('\r\n')))


def histogram(s):
	d = dict()
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[c] += 1

	return d


def choise_from_hist(dict):
	variants = []
	for word, frequency in dict.iteritems():
		variants.extend([word] * frequency)

	return choice(variants)


print choise_from_hist(histogram(lst))
