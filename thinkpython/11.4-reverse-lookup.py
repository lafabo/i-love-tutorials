#!/usr/bin/env python
# -*- coding: utf-8 -*-


def reverse_lookup(d, v):
	ret = []
	for k in d:
		if d[k] == v:
			ret.append(k)

	return ret


d = {'sister': 'anna', 'brother': 'mike', 'mother': 'anna'}

print d
print 'anna: ', reverse_lookup(d, 'anna')
print 'bill: ', reverse_lookup(d, 'bill')