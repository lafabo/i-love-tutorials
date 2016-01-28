def gcd(a, b):
	while a != 0:
		a, b = b % a, a
	return b

print gcd(int(input('greatest common divisor\nEnter a: ')), int(input('Enter b: ')))
