#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
from PIL import Image


dirname = os.path.abspath(sys.argv[1])
try:
	newdir = os.path.abspath(sys.argv[2])
except:
	newdir = dirname

def imgsort(dirname, newdir, recur=0):
	print('Sorting in %s' % dirname)
	img_list = []
	if os.path.isdir(dirname):
		for x in os.listdir(dirname):
			absx = dirname + os.sep + x
			if os.path.isfile(absx):
				img_list.append(absx)
			else:
				imgsort(absx, newdir+os.sep+x, recur=1)

		for name in img_list:
			try:
				res = Image.open(name).size
			except IOError:
				print('Seems %s is not image' % name)
				continue

			img_dir = '%sx%s' % (res[0], res[1])
			img_dir = os.path.join(newdir, img_dir)

			if os.path.split(dirname)[-1] == os.path.split(img_dir):
				continue
			elif not os.path.exists(img_dir):
				os.mkdir(img_dir)
			try:
				os.system('move "%s" "%s"' % (name, img_dir))
			except:
				print('Error moving %s' % (img_dir+'/'+name))

	if not recur:
		print('Sorting complited')


if __name__ == '__main__':
	imgsort(dirname, newdir)