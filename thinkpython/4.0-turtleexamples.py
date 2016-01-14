from swampy.TurtleWorld import *
from math import pi

world = TurtleWorld()
'''
bob = Turtle()
print (bob)

for i in range(4):
	fd(bob, 100)
	lt(bob)
'''



def square(t, len):
	for j in range(4):
		fd(t, len)
		lt(t)

len = 120
# print square(bob, len)


def polygon(t, len, n):
	angle = 360.0 / n
	polyline(t, n, len, angle)


# print polygon(bob, 12, 16)


trtl = Turtle()


def circle(t, r):
	arc(t, r, 360)


def arc(t, r, angle):
	total_len = 2 * pi * r * angle / 360
	n = int(total_len / 3) + 1
	step_len = total_len / n
	step_ang = float(angle) / n
	t.delay = 0.01
	polyline(t, n, step_len, step_ang)


def polyline(t, n, len, angle):
	for i in range(n):
		fd(t, len)
		lt(t, angle)

circle(trtl, 30)
arc(trtl, 72, 68)

wait_for_user()