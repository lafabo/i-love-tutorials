def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n+1)


def factorial(n):
	if not isinstance(n, int):
		print 'n isnt int'
		return None
	elif n < 0:
		print 'n is < than 0'
		return None
	elif n == 0:
		return 1
	else:
		return n * factorial(n-1)

print factorial(12)
