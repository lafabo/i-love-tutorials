#!/usr/bin/env python
# -*- coding: utf-8 -*-


# todo
# this script totally not working
# i'l make it one day

from datetime import datetime

lst =[]
for i in open('words.txt').readlines():
	lst.append(i.split('\r\n')[0])


# The simplest and slowest way:
time1 = datetime.now()
for i in lst:
	if (i not in dub) and (i[::-1] in lst):
		dub.append(i)
		dub.append(i[::-1])

		# print i, " : ", i[::-1]
print float(len(dub)/2)
print datetime.now() - time1

