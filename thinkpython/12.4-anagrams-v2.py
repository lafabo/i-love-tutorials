#!/usr/bin/env python
# -*- coding: utf-8 -*-

lst = []
for i in open('words.txt'):
	lst.extend(list(i.splitlines()))


def is_anagram(w1, w2):
	if len(w1) == len(w2):
		if tuple(sorted(w1)) == tuple(sorted(w2)):
			return True

	return False


def process_list(wordslist):
	result_dict = {}
	for word in wordslist:
		# if all books in the word newer appear in the dict befor
		# we added a key = this sorted list and look for all words in the wordslist
		if tuple(sorted(word)) not in result_dict.keys():
			anagrams = []
			for look_another_anagrams in wordslist:  # this also will find the var word in the wordslist
				if is_anagram(look_another_anagrams, word):

					anagrams.append(look_another_anagrams)
					# to speedup process we should del processed elements from words list
					# if look_another_anagrams != word:
					# wordslist.remove(look_another_anagrams)   # del from wordslist fonded anagrams

			result_dict[tuple(sorted(word))] = anagrams
			print tuple(sorted(word)) , ':\t', result_dict[tuple(sorted(word))]

		# if you see this - the word with some previous
		#  letters-sets was not deleted from words-list
		else:
			print 'WARNING', word

	return result_dict

test_list = ['qwe', 'qew', 'eqw', 'ewq',
             'as', 'sa',
             'ghy']

print process_list(lst)
