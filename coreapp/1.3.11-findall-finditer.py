#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

if __name__ == '__main__':
	print re.findall('car', 'car')
	print re.findall('car', 'scary')
	print re.findall('car', 'carry the thing to the car')
