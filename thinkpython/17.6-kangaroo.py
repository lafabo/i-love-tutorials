#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Kangaroo(object):
	def __init__(self):
		self.bag_contents = list()

	def put_in_bag(self, other):
		self.bag_contents.append(other)

	def __str__(self):
		return "%s" % self.bag_contents


if __name__ == '__main__':
	kanga = Kangaroo()
	roo = Kangaroo()

	print kanga
	print roo

	kanga.put_in_bag(roo)

	print kanga
	print roo