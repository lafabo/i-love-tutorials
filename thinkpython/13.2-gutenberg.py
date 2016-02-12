#!/usr/bin/env python
# -*- coding: utf-8 -*-
import string

# # # # # # # # # # # # # # # #
# prepare
text = open('d-idio.txt').read().lower()
escapes = string.punctuation.split() + string.whitespace.split()
text = text.translate(None, str(escapes)).split()

dont_use_this_words = []
for i in open('words.txt'):
	dont_use_this_words.extend(list(i.splitlines()))
# end prepare
# # # # # # # # # # # # # # # #

print 'total words in text: ', len(text)


def count_same_words(lst):
	d = dict()
	for c in lst:
		d[c] = d.get(c, 0) + 1
	return d


def most_frequent(dict):
	counter = 0
	for v in reversed(sorted(dict.values())):
		if counter < 21:
			for key in dict:
				if dict[key] == v:
					print key, v
		else:
			break

		counter += 1


def return_difference(list1, list2):
	return list(set(list1) - set(list2))


most_frequent(count_same_words(text))

print 'words in book and not in english dictionary:', len(return_difference(text, dont_use_this_words))


# todo i missed to skip the intro