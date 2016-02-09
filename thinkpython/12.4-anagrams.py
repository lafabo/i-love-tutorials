#!/usr/bin/env python
# -*- coding: utf-8 -*-

lst = []
for i in open('words.txt'):
	lst.extend(list(i.strip('\r\n')))


def has_anagrams(word, list):
	result =  {}
	for word in list:
		chars_set = list(word)
		for candidate in list:
			if len(candidate) != len(chars_set):
				continue

			for char in candidate:
				if char not in chars_set:
					continue
		val = result[tuple(chars_set)]
		result.setdefault(val, []).append(w)

		



	return dict


def most_frequent(dict):
	for v in reversed(sorted(dict.values())):
		for key in dict:
			if dict[key] == v:
				print key, v
				break


most_frequent(count_letters(lst))
