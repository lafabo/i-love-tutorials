try:
	print_something()
	print_print_something
except NameError:
	print 'Error'

def print_something():
	for i in range(10):
		print i,

def print_print_something():
	print print_something(), 'ha'

print_print_something()