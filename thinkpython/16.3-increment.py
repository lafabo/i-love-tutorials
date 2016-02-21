#!/usr/bin/env python
# -*- coding: utf-8 -*-
from copy import copy


class Time(object):
	"""
	time h:m:s
	"""


def increment(time, seconds):
	time.s += seconds
	while time.s >= 60:
		time.s -= 60
		time.m += 1
	while time.m >= 60:
		time.m -= 60
		time.h += 1

	return time


def pure_increment(time, s):
	time.s += s
	if time.s >= 60:
		time.m += time.s % 60
		time.s %= 60

	if time.m >= 60:
		time.h += time.m // 60
		time.m %= 60

	return time


def sum_increment(time, s):
	hou = time.h
	mnu = time.m
	sec = time.s + s

	if sec >= 60:
		mnu += sec // 60
		sec %= 60
	if mnu >= 60:
		hou += mnu // 60
		mnu %= 60
	if hou >= 24:
		hou = 24 - hou

	new_time = Time()
	new_time.h = hou
	new_time.m = mnu
	new_time.s = sec
	return new_time


def print_time(time):
	print '%.2d:%.2d:%.2d' % (time.h, time.m, time.s)


if __name__ == '__main__':
	t1 = Time()
	t1.h = 12
	t1.m = 57
	t1.s = 29

	t2 = copy(t1)
	t3 = copy(t1)

	print_time(increment(t1, 32))
	print_time(pure_increment(t2, 32))
	print_time(sum_increment(t3, 32))

