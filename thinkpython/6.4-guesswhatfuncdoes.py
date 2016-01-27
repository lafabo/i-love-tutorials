def b(z):
	prod = a(z,z)
	print z, prod
	return prod

def a(x, y):
	x += 1
	return x * y

def c(x, y, z):
	sum = x + y + z
	pow = b(sum) ** 2
	return pow

x = 1
y = x + 1

print(c(x, y+3, x+y))

# x = 1, y = 2
# c(1, 4, 3)
# c sum = 1 + 2 + 3
# c pow = b(1+2+3) ** 2
#   b(6)
#   b prod = a(6, 6)
#       a(6, 6)
#       a: x = 7
#       a return 6 * 7 =  42
#   b prod = 42
#   b print 6, 42
#   b return 42
# c pow = 42 ** 2 = 1764
# c return 1764

s = (c(x, y+3, x+y))

if s != 1764:
	print 'Your guess is wrong'
