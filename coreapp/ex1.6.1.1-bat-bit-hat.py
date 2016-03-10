#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

if __name__ == '__main__':
	pattern = r'[b|h][a|i|u]t'
	phrase = 'bat, bit, but, hat, hit, hut, bul, hkl'
	srch = re.findall(pattern, phrase)
	print srch