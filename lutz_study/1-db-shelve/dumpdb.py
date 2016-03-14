#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shelve

with shelve.open('peoples') as db:
	for key in db:
		print(key, '=>\n', db[key])
