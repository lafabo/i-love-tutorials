#!/usr/bin/env python
#-*- coding: utf-8 -*-

import datetime

lst = []

start = datetime.datetime.now()
for i in open('words.txt'):
	lst.append(i.split())

print datetime.datetime.now() - start


lst = []

start = datetime.datetime.now()
for i in open('words.txt'):
	lst += i.split()

print datetime.datetime.now() - start
