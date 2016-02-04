#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_anagram(word1, word2):
	#if len(list(word1)) != len(list(word2)):
	#	return False
	if sorted(list(word1.lower())) != sorted(list(word2.lower())):
		return False
	return True

print is_anagram('lisp', 'lips')
print is_anagram('Hot water', 'Worth tea')
