#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Time(object):
	"""
	Yes, this is a time
	"""


def time2int(time):
	sec = time.h * 3600 + time.m * 60 + time.s
	return sec


def int2time(integer):
	new_time = Time()
	new_time.h, rest = divmod(integer, 3600)
	new_time.m, new_time.s = divmod(rest, 60)
	return new_time


def mul_time(time, num):
	return int2time(time2int(time) * num)


def average_speed(time, distance):
	# dist / time
	average_spd = time2int(time) / distance
	return mul_time(time, average_spd)


def print_time(time):
	print '%.2d:%.2d:%.2d' % (time.h, time.m, time.s)


if __name__ == '__main__':
	t1 = Time()
	t1.h = 1
	t1.m = 2
	t1.s = 3

	t2 = time2int(t1)
	print(t2)

	print_time(int2time(t2))
	print_time(mul_time(t1, 5))
	print_time(average_speed(t1, 1500))                         # i'm afraid i don't know is it working
