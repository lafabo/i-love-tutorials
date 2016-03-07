#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

if __name__ == '__main__':
	pattern = re.compile(r'foo')
	m = re.match(pattern, 'foobar')
	b = re.match(pattern, 'barfoo')

	if m is not None: print m.group()
	if b is not None: print b.group()
