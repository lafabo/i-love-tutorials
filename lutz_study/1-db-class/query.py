#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shelve

fieldnames = 'name', 'age', 'job', 'pay'
maxfield = max(len(f) for f in fieldnames)


if __name__ == '__main__':
	with shelve.open('peoples') as db:
		while True:
			key = input('\nKey?: ')

			if not key:
				break
			else:
				try:
					record = db[key]
				except:
					print('No such key "%s"' % key)
				else:
					for field in fieldnames:
						print(field.ljust(maxfield), '=>', getattr(record, field))