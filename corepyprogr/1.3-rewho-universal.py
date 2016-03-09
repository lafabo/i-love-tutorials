#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from distutils.log import warn as printf
import re


if __name__ == '__main__':
	with os.popen('who', 'r') as f:
		for line in f:
			printf(re.split(r'\s\s+|\t', line.strip()))
