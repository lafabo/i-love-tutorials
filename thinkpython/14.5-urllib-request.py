#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests


if __name__ == '__main__':
	conn = requests.get('http://thinkpython.com/secret.html')
	for line in conn:
		print line.strip()
