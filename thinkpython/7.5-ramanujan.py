# https://epequeno.wordpress.com/2011/11/25/exercise-7-5/
# thanks dude!

from math import sqrt, factorial, pi

def estimate_pi():
	k = 0
	last = 1.0
	sigma = 0
	while last > 1e-15:
		last = (factorial(4.0*k)*(1103.0+26390.0*(k))) \
		       /((factorial(k)**4.0)*(396.0**(4.0*k)))
		k += 1.0
		sigma += last

	result = ((2*sqrt(2))/9801)*sigma
	print 1/result

estimate_pi()
print pi
