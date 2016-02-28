#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return 'x: %s, y: %s' % (self.x, self.y)

	def __add__(self, other):
		if isinstance(other, tuple):
			return self.add_tuple(other)
		else:
			return self.add_point(other)

	def __radd__(self, other):
		return self.__add__(other)

	def add_point(self, other):
		return Point(self.x + other.x, self.y + other.y)

	def add_tuple(self, other):
		return Point(self.x + other[0], self.y + other[1])


def print_attributes(obj):
		for attr in obj.__dict__:
			print(attr, getattr(obj, attr))


if __name__ == '__main__':
	a = Point(34, 52)
	b = Point(12, 12)
	c = a + b

	print(a)
	print(a + b)
	print(c)
	print type(c)
	print(a + (100, 100))
	print((100, 100) + a)
	print_attributes(Point)