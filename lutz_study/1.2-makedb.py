#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


dbfilename = 'peoples'
ENDDB = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'


def storeDbase(db, dbfilename=dbfilename):
	with open(dbfilename, 'w') as dbfile:
		for key in db:
			print(key, file=dbfile)
			for name, value in db[key].items():
				print(name + RECSEP + repr(value), file=dbfile)
			print(ENDDB, file=dbfile)


def loadDbase(dbfilename=dbfilename):
	with open(dbfilename) as dbfile:
		sys.stdin = dbfile
		db = {}
		key = input()
		while key != ENDDB:
			rec = {}
			field = input()
			while field != ENDREC:
				name, value = field.split(RECSEP)
				rec[name] = eval(value)
				field = input()
			db[key] = rec
			key = input()
		return db


if __name__ == '__main__':
	for initdata import db
	storeDbase(db)