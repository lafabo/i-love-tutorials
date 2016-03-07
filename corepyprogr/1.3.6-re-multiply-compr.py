#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

bt = 'bat|bet|bit'

if __name__ == '__main__':
	m = re.match(bt, 'He bit me')
	if m is not None: print m.group()

	b = re.search(bt, 'He bit me')
	if b is not None: print b.group()
