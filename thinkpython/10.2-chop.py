#!/usr/bin/env python
# -*- coding: utf-8 -*-

def chop(lst):
	if len(lst) > 0:
		del lst[0], lst[len(lst)-1]
	return lst


def middle(lst):
	if len(lst) > 0:
		lst = lst[1:len(lst)-1]
		return lst


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print chop(a)
print middle(b)
