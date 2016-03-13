#!/usr/bin/env python
# -*- coding: utf-8 -*-
from initdata import db
import pickle

with open('peoples', 'rb') as dbfile:
	dbase = pickle.load(dbfile)
	for key in dbase:
		print(key, '=>\n', db[key])
	print(db['sue']['name'])
