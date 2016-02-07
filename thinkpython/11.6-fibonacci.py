#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime

################
#      old     #
def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n - 2)

#  endold    #
################

known = {0: 0, 1: 1}
def fibonacci_memo(n):
	if n in known:
		return known[n]
	res = fibonacci_memo(n-1) + fibonacci_memo(n - 2)
	known[n] = res
	return res


start = datetime.now()
fibonacci(12)
print datetime.now() - start


start = datetime.now()
fibonacci_memo(12)
print datetime.now() - start
