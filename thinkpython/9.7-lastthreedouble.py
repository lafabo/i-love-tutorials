from re import match, search


def is_doubled(word):
	if match(r'([a-z])\1([a-z])\2([a-z])\3', word):
		print word


for l in open('words.txt'):
	l = l.strip()
	is_doubled(l)


