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
		fd(t, -len)
		lt(t)

len = 120
# print square(bob, len)


def polygon(t, len, n):
	angle = 360.0 / n
	for i in range(int(n)):
		fd(t, len)
		lt(t, angle)


# print polygon(bob, 12, 16)


trtl = Turtle()
print trtl


def circle(t, r):
	total_n = 50
	total_len = r * 2 * pi / total_n
	t.delay = 0.01
	print polygon(t, total_len, total_n)

circle(trtl, 30)

def arc(t, r, angle):
	n = 360.0 / angle
	# total_len = r * 2 * pi / n
	t.delay = 0.01
	for i in range(int(n)):
		fd(t, len)
		lt(t, angle)

arc(trtl, 24, 360)

wait_for_user()