#!/usr/bin/env python
# -*- coding: utf-8 -*-
from initdata import tom
import shelve

with shelve.open('peoples') as db:
	sue = db['sue']
	sue['pay'] *= 1.50
	db['sue'] = sue
	db['tom'] = tom
