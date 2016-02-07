#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from bisect import bisect_left

lst =[]
for i in open('words.txt').readlines():
	lst.append(i.split('\r\n')[0])


# The simplest and slowest way:
dub = []
time1 = datetime.now()
for i in lst:
	if (i not in dub) and (i[::-1] in lst):
		dub.append(i)
		dub.append(i[::-1])

		# print i, " : ", i[::-1]
print float(len(dub)/2)
print datetime.now() - time1

'''
# Using bisect method:
dub2 = []
time2 = datetime.now()
for i in lst:
	if (i not in dub2) and (i[::-1] not in dub2) and (bisect_left(lst, i[::-1])):
		dub2.append(i)
		dub2.append(i[::-1])
print float(len(dub2)/2)
print datetime.now() - time2
'''

# output

# i in list
# 488.0
# 0:06:58.138411

# bisect method and my algorithm
# 113411.0 <- more pares, then words in the file! awesome! todo fix this bug
# 0:06:41.011964 <- awesome economy! 17 seconds!

