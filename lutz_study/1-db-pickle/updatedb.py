#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pickle

with open('peoples', 'rb') as dbfile:
	db = pickle.load(dbfile)

	db['sue']['pay'] *= 1.10
	db['tom']['name'] = 'Tom Pot'

	with open('peoples', 'wb') as dbfile:
		pickle.dump(db, dbfile)
