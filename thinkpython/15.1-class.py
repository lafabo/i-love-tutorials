#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import sqrt
from copy import copy, deepcopy


class Point(object):
	"""
	here is point
	"""


class Rectangle(object):
	"""
	here is an rectangle
	"""


def find_center(box):
	p = Point()
	p.x = box.corner.x + box.width / 2.0
	p.y = box.corner.y + box.height / 2.0
	return p


def get_distance(point1, point2):
	# d = sqrt ( (x2 - x1) ** 2 + (y2 - y1) ** 2 )
	d = sqrt((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2)
	return d


def print_point(p):
	print '(%g, %g)' % (p.x, p.y)


def move_rectangle(rect, dx, dy):
	rect.corner.x += dx
	rect.corner.y += dy
	return rect


def move_to_new_rectangle(rect, dx, dy):
	newrect = deepcopy(rect)
	newrect.corner.x += dx
	newrect.corner.y += dy
	return newrect



if __name__ == '__main__':
	p1 = Point()
	p1.x = 1.0
	p1.y = 4.0
	p2 = Point()
	p2.x = 2.0
	p2.y = 1.0

	print 'distance between p1(%s, %s) and p2(%s, %s)' \
	      ' = ' % (p1.x, p1.y, p2.x, p2.y), get_distance(p1, p2)

	box = Rectangle()
	box.width = 100.0
	box.height = 200.0
	box.corner = Point()
	box.corner.x = 0.0
	box.corner.y = 0.0

	center = find_center(box)
	print_point(center)

	print move_rectangle(box, 10.0, 12.0)
	print move_to_new_rectangle(box, 10.0, 12.0)
	print move_rectangle(box, 10.0, 12.0) is move_to_new_rectangle(box, 10.0, 12.0)
