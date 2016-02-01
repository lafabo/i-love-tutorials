# short answer: 337

def is_abecederian(string):
	prev_letter = ''
	for letter in string:
		if letter <= prev_letter:
			return False
		prev_letter = letter
	return True


f = open('words.txt')
abclike = 0
total = 0
for l in f:
	l = l.strip()
	if is_abecederian(l):
		abclike += 1
	total += 1


print abclike, 'of total ', total
