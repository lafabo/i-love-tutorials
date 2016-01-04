from math import fabs

def gcd(a, b):
	while a != 0:
		a, b = b%a, a
	return b

def lcm(a,b):
	return fabs(a * b) / gcd(a, b)

print lcm(int(input('greatest common divisor\nEnter a: ')), int(input('Enter b: ')))