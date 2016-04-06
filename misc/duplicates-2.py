#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import hashlib


def hashfile(path, blocksize=65536):
	with open(path, 'rb') as afile:
		hasher = hashlib.md5()
		buf = afile.read(blocksize)
		while len(buf) > 0:
			hasher.update(buf)
			buf = afile.read(blocksize)
	return hasher.hexdigest()


def get_files_list(path):
	exten = '.jpg'
	result = []
	for dirpath, dirnames, filenames in os.walk(path):
		for name in filenames:
			if name.lower().endswith(exten):
				result.append(os.path.join(dirpath, name))
	# return list
	return result



if __name__ == '__main__':
