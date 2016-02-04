#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_sorted(lst):
	if sorted(lst) == lst:
		return True
	else:
		return False


print is_sorted([1, 3, 2])
print is_sorted([1, 2, 3])
