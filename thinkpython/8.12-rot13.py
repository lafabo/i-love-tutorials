def rotate_word(word, num=13):
	new_word = u''
	for i in word:
		new_letter = ord(i) + num
		new_word += unicode(chr(new_letter))

	return new_word


print rotate_word('cheer', 7)
print rotate_word('melon', -10)
