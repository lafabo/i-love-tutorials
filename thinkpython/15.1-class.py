#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import sqrt


class Point(object):
	""" point x, y"""
	def __init__(self, x, y):
		self.x = x
		self.y = y


class Rectangle(object):
	def __init__(self, width, height, corner):
		self.width = width
		self.height = height
		self.corner = Point


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
	pass

if __name__ == '__main__':
	p1 = Point(1, 4)
	p2 = Point(5, 2)

	print get_distance(p1, p2)

	center = find_center(box)
	# print_point
