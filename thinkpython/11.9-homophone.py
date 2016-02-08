#!/usr/bin/env python
# -*- coding: utf-8 -*-

def make_words_list():
	lst = []
	for i in open('words.txt'):
		if len(i.strip('\r\n')) > 2:
			lst.append(i.strip('\r\n'))
	return lst


def read_dictionary():
	d = dict()
	fin = open('c06d.txt')
	for line in fin:
		t = line.split()
		if len(t[0]) > 2:
			word = t[0].lower()
			pron = ' '.join(t[1:])
			d[word] = pron

	return d


def check(pron_dict, words_list):
	for word in words_list:
		w1 = word[1:]
		w2 = word[0]+word[2:]
		if word in pron_dict and w1 in pron_dict and w2 in pron_dict:
			if pron_dict[word] == pron_dict[w1] and pron_dict[word] == pron_dict[w2]:
				print word, ' - ', pron_dict[word], '\t', w1, ' - ', pron_dict[w1], '\t', w2, ' - ', pron_dict[w2]


check(read_dictionary(), make_words_list())
