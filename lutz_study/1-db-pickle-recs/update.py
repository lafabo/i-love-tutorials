#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pickle

with open('sue.plk', 'rb') as suefile:
	sue = pickle.load(suefile)

sue['pay'] *= 1.10

with open('sue.plk', 'wb') as suefile:
	pickle.dump(sue, suefile)
