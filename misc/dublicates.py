#!/usr/bin/env python
# -*- coding: utf-8 -*-
# well, i have not one mp3 file on PC, so i change quest to .jpg
import os
import hashlib
from collections import defaultdict


def get_files_list(path):
	exten = '.jpg'
	result = []
	for dirpath, dirnames, filenames in os.walk(path):
		for name in filenames:
			if name.lower().endswith(exten):
				result.append(os.path.join(dirpath, name))
	# return list
	return result


def get_md5(lst):
	result_dict = defaultdict(list)
	for filename in lst:
		with open(filename, 'rb') as currentfile:
			md5hash = hashlib.md5(currentfile.read()).hexdigest()
			result_dict[md5hash].append(filename)
	# return dict, key = md5hash, value = [dub1, dub2...]
	return result_dict


if __name__ == '__main__':
	path = '/home/i/Pictures/'
	# print get_files_list(path)
	# print get_md5(get_files_list(path))
	hui = get_md5(get_files_list(path))
	itera = 1
	for k in hui:
		if len(hui[k]) > 1:
			print itera, k, ':', hui[k]
			itera += 1
