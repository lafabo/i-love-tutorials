"""
Module provide simple Turtle drawing methods

Polyline draws all lines, other definitions draw primitives with polyline:
"""
from swampy.TurtleWorld import *
from math import pi

def polyline(turtle, polygons, length, angle):
	for j in range(polygons):
		fd(turtle, length)
		lt(turtle, angle)

def square(turtle, length):
	polyline(turtle, 4, length, 90)


def polygon(turtle, polygons, length):
	angle = int(360.0 / polygons)
	polyline(turtle, polygons, length, angle)

def arc(turtle, radius, angle):
	arc_len = 2 * pi * radius * angle / 360
	polygons = int(arc_len / 3) + 1
	step_len = arc_len / polygons
	step_angle = float(angle / polygons)
	polyline(turtle, polygons, step_len, step_angle)


def circle(turtle, radius):
	arc(turtle, radius, 360)

world = TurtleWorld()
bob = Turtle()

# tests:
# print square(bob, 15)
# print polygon(bob, 8, 35)
# print circle(bob, 15)
# print arc(bob, 120, 24)


# flowers
bob.delay = 0.01


def flower(turtle, radius, angle):
	fl_range = 2 * pi * radius * angle / 360
	for i in range(0, radius):
		if i % 2 != 0:
			print arc(turtle, fl_range, angle)
			rt(bob, 360-angle)
		else:
			print arc(turtle, fl_range, angle)
			lt(bob, 360-angle)


print flower(bob, 20, 27)

wait_for_user()
