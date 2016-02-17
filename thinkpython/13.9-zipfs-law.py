#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import Counter

lst = []
for i in open('words.txt'):
	lst.extend(list(i.strip('\r\n')))


def sort_and_rank(lst):
	c = Counter()
	for word in d:
		c[word] += 1

	return c


# todo write this script!