#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randrange, choice
from string import ascii_lowercase as lc
from sys import maxint
from time import ctime

tlds = ('com', 'edu', 'net', 'org', 'gov')

if __name__ == '__main__':
	for i in xrange(randrange(5, 11)):
		dtint = randrange(maxint)       # date
		print dtint
		dtstr = ctime(dtint)            # date str
		print dtstr
		llen = randrange(4, 8)          # domain name
		login = ''.join(choice(lc) for j in range(llen))
		dlen = randrange(llen, 13)      # longer domain name
		dom = ''.join(choice(lc) for j in xrange(dlen))
		print '%s::%s@%s.%s::%d-%d-%d' % (dtstr, login, dom, choice(tlds),
		                                  dtint, llen, dlen)
