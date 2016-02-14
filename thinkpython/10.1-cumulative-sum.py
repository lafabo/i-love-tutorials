#!/usr/bin/env python
# -*- coding: utf-8 -*-


def cumulative_sum(lst):
	new = []
	try:
		last = 0
		for i in lst:
			new.append(i + last)
			last += i
	except ValueError:
		print 'not a number in the list'

	return new


print cumulative_sum([1, 2, 3])
