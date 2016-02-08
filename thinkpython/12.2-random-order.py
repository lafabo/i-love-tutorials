#!/usr/bin/env python
# -*- coding: utf-8 -*-


def sort_by_length(words):
	t = []
	for word in words:
		t.append((len(word), word))

	t.sort(reverse=True)
	res = []
	for length, word in t:
		res.append(word)
	return res


def sort_by_length_random(words):
	t = []