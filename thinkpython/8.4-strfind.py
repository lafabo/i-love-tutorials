def find(word, letter, index=0):
	start = index
	while index < len(word):
		if word[index] == letter:
			return '%s in word %s (search started from %s) has index %s' % (letter, word, start, index)
		index += 1
	return -1


print find('Contribution', 'n', 7)

