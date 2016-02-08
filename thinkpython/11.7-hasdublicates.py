#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import Counter


def has_duplicates(lst):
	c = Counter()
	for item in lst:
		c[item] += 1
		if c[item] > 1:
			return True
	return False


print 'True if has dublicates'
print has_duplicates([1, 2, 3, 5, 6, 6, 7, 4, 6])
print has_duplicates([1, 2, 3])
print has_duplicates(['anna', 'bill', 'anna'])