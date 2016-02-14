#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string
from random import choice


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


def most_common(h):
	t = []
	for k, v in h.items():
		t.append((v, k))
	t.sort(reverse=True)
	return t


def print_most_common(h, num=10):
	print '10 most common words:'
	for f, w in most_common(h)[:num]:
		print w, '\t', f


def subtract(d1, d2):
	res = dict()
	for key in d1:
		if key not in d2:
			res[key] = None

	return res


def random_word(h):
	t = []
	for w, f in h.items():
		t.extend([word] * f)
	return choice(t)

# Exercise 13.7
def random_word_optimized(h):
	t = []
	for w in h:
		t.extend(w * h[w])
	return t


def cumulative_words_sum(h):
	new = []
	last = 0
	for i in h.values():
		new.append(i + last)
		last += i

	return new


def bisectional_search(h):
	pass


# todo № 2, 3, 4 - i'm really don't understand what author asks to program



hist = process_file('d-idio.txt')

print 'Words: \t\t\t', total_words(hist)
print 'Different words: \t', different_words(hist)
print print_most_common(hist, 20)

print 'Words in book and not in english dictionary:'
for word in subtract(hist, process_file('words.txt')).keys():
	print word,
print '\n\n'
print 'Random word:', random_word(hist)
