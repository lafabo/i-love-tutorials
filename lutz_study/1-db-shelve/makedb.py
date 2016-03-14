#!/usr/bin/env python
# -*- coding: utf-8 -*-
from initdata import bob, sue, tom
import shelve

with shelve.open('peoples') as db:
	db['bob'] = bob
	db['sue'] = sue
