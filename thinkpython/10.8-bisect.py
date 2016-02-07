#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bisect

lst =[]
for i in open('words.txt').readlines():
	lst.append(i.split('\r\n')[0])


def check_is_word_in_list(lst, word):
	return bisect.bisect_left(lst, word)

# print check_is_word_in_list(lst, 'weather')


def f(x):
	return x**3 + x -1


def bisection(sorted_list, word):
	min = 0
	max = len(sorted_list) - 1

	while True:
		i = (min + max) / 2

		if max < min:
			return None

		if word == sorted_list[i]:
			return i
		elif word < sorted_list[i]:
			max = i - 1
		else:
			min = i + 1


print bisection(lst, 'python')
print check_is_word_in_list(lst, 'python')
print lst[78834]