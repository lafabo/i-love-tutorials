# some code from the book

def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]

# endbookcode


def is_palindrome(word):

	if word[:] != word[::-1]:
		print word, 'not a palindrome'
		return True
	else:
		print word, 'is a palindrome'
		return False

is_palindrome('doom')
is_palindrome('quake')
is_palindrome('qweewq')
is_palindrome('mom')

