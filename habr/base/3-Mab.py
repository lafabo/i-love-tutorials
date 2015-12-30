print 'Print all i*M in range(a, b)'
M = int(raw_input('Enter M: '))
a = int(raw_input('Enter a: '))
b = int(raw_input('Enter b: '))

if a > b:
	a, b = b, a

for i in range(a, b+1):
	print '%s * %s = ' % (i, M), M*i
