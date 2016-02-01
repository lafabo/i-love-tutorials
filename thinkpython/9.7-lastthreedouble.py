import re

def is_doubled(word):
	# damstupidpattern
	c5,c4,c3,c2,c1=''
	for i in len(word):
		if (word[i-5]==word[i-4] and word[i-3]==word[i-2] and word[i-1]==word[i]):
			print word


f = open('words.txt')
for l in f:
	l = l.strip()
	is_doubled(l)


