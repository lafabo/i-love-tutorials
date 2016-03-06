#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, re

if __name__ == '__main__':
	f = os.popen('who', 'r')
	for eachline in f:
		print re.split(r'\s\s+|\t', eachline.rstrip())
	f.close()
