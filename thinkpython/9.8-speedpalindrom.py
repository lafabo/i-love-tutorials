def is_palindrom(num, digit):       # digit - to skip something in the xxxxxx-num
	testthis = str(num)[digit:]
	# print testthis, num
	if testthis == testthis[::-1]:
		return True

for i in xrange(99999, 1000000):
	if is_palindrom(i, 0) and is_palindrom(i-1, 1) and is_palindrom(i-2, 2):
		print i, i-1, i-2
