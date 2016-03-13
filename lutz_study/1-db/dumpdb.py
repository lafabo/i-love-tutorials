#!/usr/bin/env python
# -*- coding: utf-8 -*-
from makedb import loadDbase

db = loadDbase()

for key in db:
	print(key, '=>\n', db[key])
print(db['sue']['name'])
