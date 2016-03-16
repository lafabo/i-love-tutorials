#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shelve
from dbclasses import Person
fieldnames = ('name', 'age', 'job', 'pay')

if __name__ == '__main__':
	with shelve.open('peoples') as db:
		while True:
			key = input('\nKey: ')
			if not key:
				break
			if key in db:
				record = db[key]
			else:
				record = Person(name='?', age='?')

			for field in fieldnames:
				currval = getattr(record, field)
				nexttext = input('\t[%s]=%s\n\t\tnew?=>' % (field, currval))
				if nexttext:
					setattr(record, field, eval(nexttext))

			db[key] = record