#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shelve
from dbclasses import Person, Manager
from initdata import bob, sue, tom


if __name__ == '__main__':
	with shelve.open('peoples') as db:
		db['bob'] = bob
		db['sue'] = sue
		db['tom'] = tom
