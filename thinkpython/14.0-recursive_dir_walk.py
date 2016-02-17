#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


def walk(dir):
	filelist = []
	for name in os.listdir(dir):
		path = os.path.join(dir, name)
		if os.path.isfile(path):
			filelist.append(path)
		else:
			walk(path)

	return filelist


print walk('/home/i/dev/i-love-tutorials/thinkpython')

print '\n\n\n\n'
for i in os.walk('/home/i/dev/i-love-tutorials/thinkpython'):
	print i
