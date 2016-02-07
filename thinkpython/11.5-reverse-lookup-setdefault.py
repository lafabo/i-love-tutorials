#!/usr/bin/env python
#-*- coding: utf-8 -*-


def invert_dict(d):
	inv = dict()
	for key in d:
		val = d[key]
		inv.setdefault(val, []).append(key)
	return inv


d = {'sister': 'anna', 'brother': 'mike', 'mother': 'anna'}
