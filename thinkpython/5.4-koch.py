from swampy.TurtleWorld import *


def koch(turtle, x):
	"""
	:param x: length
	"""
	if x < 3:
		fd(turtle, x)
		return
	m = x / 3
	koch(turtle, m)
	lt(turtle, 60)
	koch(turtle, x/3)
	rt(turtle, 120)
	koch(turtle, x/3)
	lt(turtle, 60)
	koch(turtle, x/3)


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.001
koch(bob, 1200)

wait_for_user()