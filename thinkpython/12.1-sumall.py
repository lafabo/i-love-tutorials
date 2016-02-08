#!/usr/bin/env python
# -*- coding: utf-8 -*-


def sumall(*args):
	summ = 0
	for arg in args:
		summ += arg

	return summ

print sumall(12, 2, 34, 3, 5, -5, -4)