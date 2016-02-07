#!/usr/bin/env python
# -*- coding: utf-8 -*-


dct = {}
for i in open('words.txt'):
	k = i.strip('\r\n')
	dct[k] = '0'


def check_word(dct):
	if 'algorithm' in dct:
		return dct['algorithm']

print check_word(dct)

#print dct