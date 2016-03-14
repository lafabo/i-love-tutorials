#!/usr/bin/env python
# -*- coding: utf-8 -*-
from initdata import bob, sue, tom
import pickle

for key, value in [('bob', bob), ('tom', tom), ('sue', sue)]:
	with open(key + '.plk', 'wb') as recfile:
		pickle.dump(value, recfile)
