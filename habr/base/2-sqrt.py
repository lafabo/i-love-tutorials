from math import sqrt

print 'ax^2 + bx + d = 0'
a = float(raw_input('Enter a: '))
b = float(raw_input('Enter b: '))
c = float(raw_input('Enter d: '))

D = b**2 - 4*a*c
print 'D = ', D

if D > 0:
	x1 = (-b + sqrt(D)) / (2 * a)
	x2 = (-b - sqrt(D)) / (2 * a)
	print 'D > 0: x1 = %d, x2 = %d' % (x1, x2)
elif D == 0:
	x = - (b / (2 * a))
	print 'D = 0, x = %d' % x
else:
	print 'D < 0, no rational x'
