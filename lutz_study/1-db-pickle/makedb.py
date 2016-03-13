#!/usr/bin/env python
# -*- coding: utf-8 -*-
from initdata import db
import pickle

with open('peoples', 'wb') as dbfile:
	pickle.dump(db, dbfile)
