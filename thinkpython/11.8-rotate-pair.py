#!/usr/bin/env python
# -*- coding: utf-8 -*-

lst = []
for i in open('words.txt'):
	lst.append(i.strip('\r\n'))


def rotate_word(word, num):
	new_word = u''
	for i in word:
		new_letter = ord(i) + num
		new_word += unicode(chr(new_letter))

	return new_word

for word in lst:
	#######################################################
	# Here you can chose how big is step range or etc     #
	# range(1, 26) as a litters in ABC is a maximum range #
	#######################################################
	for i in range(1, 3):
		if rotate_word(word, i) in lst:
			print word, rotate_word(word, i)
