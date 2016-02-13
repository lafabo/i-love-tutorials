#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string


def process_file(filename):
	h = dict()
	fp = open(filename)
	for line in fp:
		process_line(line, h)

	return h


def process_line(line, h):
	line = line.replace('-', ' ')
	for word in line.split():
		word = word.strip(string.punctuation + string.whitespace)
		word = word.lower()
		h[word] = h.get(word, 0) + 1


def total_words(h):
	return sum(h.values())


def different_words(h):
	return len(h)


hist = process_file('d-idio.txt')

print 'Words: \t\t\t', total_words(hist)
print 'Different words: \t', different_words(hist)
