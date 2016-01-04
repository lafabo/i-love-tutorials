#!/usr/bin/env python
#coding: utf8
from collections import defaultdict

raw = [x.split(': ') for x in open('11chat.txt')]

# count nick-letters
wordsdict = defaultdict(int)
total = 0           # all letters

for nick, mess in raw:
	wordsdict[nick] += len(mess)
	total += len(mess)

lst = wordsdict.items()
lst.sort(key=lambda (key, val): val)

print 'Username\tLetters\tPercent'
print '\n'.join('%s\t%d\t%d' % (nick, mess, mess*100/total) for nick, mess in lst)