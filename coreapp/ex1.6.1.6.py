#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

domainslist = ['www.hhhuuuu.com', 'http://ppppi.edu']

for domain in domainslist:
	if re.match(r'(http:\/\/|www).(\w+)*?.(com|edu|net|org)', domain):
		print domain
