#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re, os

if __name__ == '__main__':
	with os.popen('who', 'r') as f:
		for eachline in f:
			print re.split(r'\s\s+|\n', eachline.rstrip())
