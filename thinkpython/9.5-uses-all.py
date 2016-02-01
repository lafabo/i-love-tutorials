def uses_only(word, letters):
	for i in letters:
		if i not in word:
			return False
	return True


def uses_all(word, strin):
	uses_only(word, strin)


print uses_all('hello', 'hleos')
print uses_all('hello', 'hlleo')
print uses_all('hello', 'hles')
