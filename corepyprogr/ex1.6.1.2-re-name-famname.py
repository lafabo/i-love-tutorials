#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

if __name__ == '__main__':
	pattern = r'\w+[ ]\w+'
	phrase = 'Anna-Maria, Mike Jordan, Papa-Buba Diup'
	srch = re.findall(pattern, phrase)
	print srch