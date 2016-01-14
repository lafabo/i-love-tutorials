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
	circle_len = 2 * pi * radius
	polygons = int(circle_len / 3) + 1
	sector_len = circle_len / polygons
	sector_angle = 360 / polygons
	polyline(turtle, polygons, sector_len, sector_angle)



# tests:
print square(bob, 15)
# print polygon(bob, 8, 35)
# print circle(bob, 15)
# print arc(bob, 120, 24)


wait_for_user()
