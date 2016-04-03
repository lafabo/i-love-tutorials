#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ReseekFile
import os


def get_files_list(path):
	result = []
	for dirpath, dirnames, filenames in os.walk(path):
		for name in filenames:
			result.append(os.path.join(dirpath, name))
	return result


def get_real_ext(filepath):
	with ReseekFile.ReseekFile(open(filepath)) as datastream:
		data = str(datastream.read(24))
		size = len(data)
		image_type = ''

		if size >= 10 and data[:6] in ('GIF87a', 'GIF89a'):
			image_type = 'image/gif'
		elif size >= 24 and data.startswith('\211PNG\r\n\032\n') and data[12:16] == 'IHDR':
			image_type = 'image/png'
		elif size >= 16 and data.startswith('\211PNG\r\n\032\n'):
			image_type = 'image/png'
		elif size >= 2 and data.startswith('\337\330'):
			image_type = 'image/jpeg'

		return image_type


def rename_file(filepath, image_type):
	ext = None

	if image_type == 'image/gif':
		ext = '.gif'
	elif image_type == 'image/png':
		ext = '.png'
	elif image_type == 'image/jpeg':
		ext = '.jpg'

	if ext and not filepath.endswith(ext):
		os.rename(filepath, str(filepath + ext))

if __name__ == '__main__':
	print('Enter the path to a directory with images without extensions')
	files_list = get_files_list(input('>: '))
	for each_file in files_list:
		#this will rename only if ext not the real
		rename_file(each_file, get_real_ext(each_file))

