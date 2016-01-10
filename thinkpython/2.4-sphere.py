from math import pi


def v(r):
	v = 4.0/3.0*pi*(r**3)
	# huh, that was interesting. Int / int not the same as float/float
	return v

print v(5.0)
