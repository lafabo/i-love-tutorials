#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gzip
import os
import sys


def unzip(path):
	filelist = os.listdir(path)
	filelist.sort()

	with open('output.txt') as op:
		for file in filelist:
			if file.endswith('.gz') or file.endswith('.zip'):
				sys.stderr.write(file+'\n')
				with gzip.open(path + file, 'rb') as f:
					file = f.read()
					op.write(file + '\n')

if __name__ == '__main__':
	path = sys.argv[1]
	unzip(path)