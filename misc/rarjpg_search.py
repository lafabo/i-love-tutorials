#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Looking for a RarJpeg files.
Not even bit optimized, but it can handle with a task

You need rar installed to use this script
i mean: $ sudo apt-get install rar
"""
import os
import imghdr

# here you can write path to look jpg and jpeg files
# search_here = ['/home/i/Pictures/rarjp/']
search_here = ['/media/i/My_D/pics/',
               '/media/i/My_D/pics1',
               '/media/i/My_D/pics2',
               '/media/i/My_D/pics3',
               '/media/i/My_E/2ch and desktops']
exts = 'jpg', 'jpeg'


def check_ext(curentfile):
	if imghdr.what(curentfile) in exts:
		return True
	return False


def check_rar(curentfile):

	if 'All OK' in os.popen('rar t "' + curentfile + '"').read():
		return True

	return False


if __name__ == '__main__':
	allfiles = []
	for current_path in search_here:
		for (dir, _, files) in os.walk(current_path):
			for f in files:
				path = os.path.join(dir, f)
				if os.path.exists(path):
					if check_ext(path) and check_rar(path):         # here is my magic!
						print path
						allfiles.append(path)
