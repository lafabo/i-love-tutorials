def avoids(word, escapes):
	for letter in word:
		if letter in escapes:
			return False
	return True


f = open('words.txt')

escapes = str(raw_input('Enter letters to skip: '))
counter = 0

for l in f:
	l = l.strip()
	if avoids(l, escapes):
		counter += 1

print 'With escape string ', escapes, ' skiped', counter, " of the 103809 words"
