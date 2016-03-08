#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

if __name__ == '__main__':
	data = (
		'Mountain View CA 94040',
		'Sunnyvale, CA',
		'Los Altos, 94023',
		'Cupertino 94014',
		'Palo Alto CA'
	)

	for datum in data:
		print re.split(', |(?= (?:\d{5}|[A-Z]{2}))', datum)
