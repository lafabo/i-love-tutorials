#!/usr/bin/env python
# -*- coding: utf-8 -*-
a = open('dealers.csv')
r = []
for k in a:
	if k.split('; ')[1] != 'no@mail':
		print(k.split('; ')[1], end=',')
