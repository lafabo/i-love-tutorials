#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

if __name__ == '__main__':
	pattern = '\w+@(\w+\.)*\w+\.com'
	hu = re.match(pattern, 'olala@www.xxx.yyy.zzz.com')
	print hu.group()