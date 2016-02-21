#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Time(object):
	"""
	time h:m:s
	"""


def time2s(t):
	return t.s + t.m*60 + t.h*3600


def is_after(t1, t2):
	return time2s(t2) > time2s(t1)


if __name__ == '__main__':
	t1 = Time()
	t2 = Time()
	t1.h = 1
	t1.m = 1
	t1.s = 1
	t2.h = 1
	t2.m = 1
	t2.s = 2

	print is_after(t1, t2)