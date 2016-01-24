print "Fermat's theorema: a ** n + b ** n != c**n if n > 2"

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
n = int(input("n: "))


def check_fermat(a, b, c, n):
	print '(%s**%s =' % (a, n), a**n, ') + (', '%s**%s =' % (b, n), b ** n, \
		') == (%s**%s =' % (c, n),  c ** n, ')'
	if a**n + b**n == c ** n and n > 2:
		print 'Fermat missed'
	else:
		print "I missed"

# pew pew
check_fermat(a, b, c, n)
