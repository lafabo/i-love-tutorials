#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Time(object):
	"""
	time h:m:s
	"""


def add_time(t1, t2):
	sum = Time()
	sum.h = t1.h + t2.h
	sum.m = t1.m + t2.m
	sum.s = t1.s + t2.s

	if sum.s >= 60:
		sum.s -= 60
		sum.m += 1

	if sum.m >= 60:
		sum.m -= 60
		sum.h += 1

	return sum


def print_time(time):
	print '%.2d:%.2d:%.2d' % (time.h, time.m, time.s)


if __name__ == '__main__':
	start = Time()
	start.h = 7
	start.m = 40
	start.s = 0

	duration = Time()
	duration.h = 1
	duration.m = 35
	duration.s = 0

	done = add_time(start, duration)
	print_time(done)