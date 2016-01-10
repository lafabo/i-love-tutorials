def check(var, guess):
	if type(var) == guess:
		print 'good\t\t %s is %s' % (var, guess)
	else:
		print "bad\t\t %s isn't %s" % (var, guess)

width = 17
height = 12.0
delimiter = '.'

check(width/2, float)       # heh, my mistake
check(width/2.0, float)
check(height/3, float)
check(1 + 2 * 5, int)
check(delimiter * 5, str)
