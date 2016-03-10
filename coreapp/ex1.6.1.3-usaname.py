#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

if __name__ == '__main__':
	pattern = r'\w+, [A-Z]'
	phrase = 'Bell, L; Dell, M; Buba M; Holly-Grail'
	print re.findall(pattern, phrase)