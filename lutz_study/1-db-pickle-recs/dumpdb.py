#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pickle, glob

for filename in glob.glob('*.plk'):
	with open(filename, 'rb') as recfile:
		record = pickle.load(recfile)
		print(filename, '=>\n', record)
