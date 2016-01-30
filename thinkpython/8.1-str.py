def reverse(string):
	for i in string[::-1]:
		print i,


def ducks():
	prefixes = 'JKLMNOPQ'
	suffix = 'ack'
	for letter in prefixes:
		if letter == 'O' or letter == 'Q':
			print(letter+'u'+suffix)
		else:
			print(letter+suffix)


reverse('mamba mamba hu')
print "\n"
ducks()
