#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Time(object):
	"""
	time of a day: h, m, s
	"""


def print_time(time):
	print '%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second)


def is_after(t1, t2):
	return t1


if __name__ == '__main__':
	time = Time()
	time.hour = 1
	time.minute = 59
	time.second = 20

	print_time(time)