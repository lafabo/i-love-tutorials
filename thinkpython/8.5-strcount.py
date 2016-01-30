def find(word, letter, index=0):
	start = index
	res = []
	while index < len(word):
		if word[index] == letter:
			res.append(index)
		index += 1

	return len(res)


def count(string, substring):
	if substring in string:
		return string.count(substring)
	else:
		return None


def count2(string,substring):
	return find(string, substring)


print count2('hello', 'l')