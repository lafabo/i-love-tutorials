#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

if __name__ == '__main__':
	m = re.search('foo', 'seafood')
	if m is not None: print m.group()