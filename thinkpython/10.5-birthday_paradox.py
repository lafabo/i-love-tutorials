#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint


def has_dublicates(lst):
	for i in lst:
		if lst.count(i) > 1:
			return False
	return True

bdays = []
for i in range(23):
	bdays.append(randint(1, 356))

print sorted(bdays)
print has_dublicates(bdays)
