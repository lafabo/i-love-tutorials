#!/usr/bin/env python
# -*- coding: utf-8 -*-
import operator, sys, datetime


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
	intera = 0
	start = datetime.datetime.now()
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
			# print tuple(sorted(word)) , ':\t', result_dict[tuple(sorted(word))]

		# if you see this - the word with some previous
		#  letters-sets was not deleted from words-list
		# else:
		# 	print 'WARNING', word

		sys.stdout.write('\r%s' % intera)
		sys.stdout.flush()

		intera += 1

	return result_dict


def find_biggest_sets(results_dict):
	sorted_results = sorted(results_dict.items(), key=operator.itemgetter(1))
	return sorted_results


def find_scrabble(wordslist):
	"""we need only 8 letters-len words, so let's get only them"""
	result = []
	for word in wordslist:
		if len(word) == 8:
			result.append(word)
	return result


def find_metathesis_pairs(wordsdict):
	"""
	so i uses the same letters but different postions of only 1 letter
	like "conVerSe" and "conSerVe"
	Check the result dict for each same-letters-keys
	"""
	pairs = {}
	num = 0
	for anagram_char_set in wordsdict.keys():
		for word1 in wordsdict[anagram_char_set]:
			for word2 in wordsdict[anagram_char_set]:
				if word2 is word1:
					continue
				counter = 0
				for c1, c2 in zip(word1, word2):
					if c1 != c2:
						counter += 1
					if counter > 2:
						continue

				pairs[num] = [word1, word2]
				num += 1
				print 'metathesis pair: ', word1, word2

	return pairs


test_list = ['qwe', 'qew', 'eqw', 'ewq',
             'as', 'sa',
             'ghy',
             'hedoff', 'jouip', 'dffdfdf', 'dffdfff', 'google', 'goolge']

#print process_list(lst)
#print process_list(test_list)
#
#for i in reversed(find_biggest_sets(process_list(test_list))):
#	print i

#for i in reversed(find_biggest_sets(process_list(lst)))[:20]:       # top 20
#	print i

#scrabble_words = find_scrabble(lst)
#print 'Scrable words: ', len(scrabble_words)
#print process_list(scrabble_words)


print find_metathesis_pairs(process_list(test_list))