f = open('words.txt', 'r')

def has_no_e(file):
	'''
	prints only words witout 'e' from the file
	'''
	without_e = 0
	words_total = 0
	for line in file:
		word = line.strip()
		if 'e' not in word:
			print word
			without_e += 1
		words_total += 1

	print '\n\n\nWords without "e" %:', without_e * 100 / words_total


has_no_e(f)
