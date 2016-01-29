from math import sqrt

def square_root(a):
	x = a / 2.0
	while True:
		y = (x + a/ x) / 2
		if abs(y - x) < 0.0000001: # here you can chose how many numbers after the dot
			break
		x = y

	return x

def build_a_table(start, stop):     # must be integer
	print 'Num\tSquareRoot\tMath.sqrt\t\tDelta'
	for i in range(start, stop+1):
		cur = float(i)
		sqroot = square_root(cur)
		mathsq = sqrt(cur)
		delta = sqroot - mathsq
		print '%s\t%s\t%s\t\t%s' % (cur, sqroot, mathsq, delta)


build_a_table(1, 9)
