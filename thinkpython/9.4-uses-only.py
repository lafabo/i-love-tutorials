def uses_only(word, letters):
	for letter in letters:
		if letter not in word:
			return False
	return True

f = open('words.txt')

letters = str(raw_input('Enter letters from which we can search hole words: '))
counter = 0

for l in f:
	l = l.strip()
	if uses_only(l, letters):
		counter += 1

print counter
