#!/usr/bin/env python
# -*- coding: utf-8 -*-
from swampy.World import World

world = World()


class Canvas(object):
	def __init__(self, width, height, background):
		self.width = width
		self.height = height
		self.background = background


class Rectangle(object):
	def __init__(self, c1x, c1y, c2x, c2y, outline, width, fill):
		self.corner1 = [c1x, c1y]
		self.corner2 = [c2x, c2y]
		self.outline = outline
		self.width = width
		self.fill = fill


class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y


class Circle(object):
	def __init__(self, x, y, rad, outline, width, fill):
		self.xy = [x, y]
		self.rad = rad
		self.outline = outline
		self.width = width
		self.color = fill


def draw_rectangle(canvas, rectangle):
	"""
	:param canvas: window setting - {width, height, background}
	:param rectangle: {type, outline, borders-size, color}
	:return:
	"""
	window = world.ca(width=canvas.width, height=canvas.height, background=canvas.background)
	rect = window.rectangle([rectangle.corner1, rectangle.corner2], outline=rectangle.outline, width=rectangle.width, fill=rectangle.fill)
	return window, rect


def draw_point(canvas, rectangle):
	window = world.ca(width=canvas.width, height=canvas.height, background=canvas.background)
	point = window.rectangle([[rectangle.corner1[0]-1, rectangle.corner1[1]-1], [rectangle.corner1[0]+1, rectangle.corner1[1]+1]],
	                         outline=rectangle.outline, width=rectangle.width, fill=rectangle.fill)

	return window, point


def draw_circle(canvas, circle):
	window = world.ca(width=canvas.width, height=canvas.height, background=canvas.background)
	drawn_circle = window.circle(circle.xy, circle.rad, outline=circle.outline, width=circle.width, fill=circle.color)

	return window, drawn_circle


def cz_flag(canvas):
	canv = world.ca(width=canvas.width, height=canvas.height, background=canvas.background)

	# flag = [[0, 0], [0, 150], [250, 150], [250, 0]]
	# canv.polygon(flag, fill='black')
	blue = [[0, 150], [100, 75], [0, 0]]
	canv.polygon(blue, fill='blue')
	white = [[0, 150], [100, 75], [250, 75], [250, 150]]
	canv.polygon(white, fill='white')
	red = [[0, 0], [100, 75], [250, 75], [250, 0]]
	canv.polygon(red, fill='red')


if __name__ == '__main__':

	canv = Canvas(500, 500, 'green')

	# DRAWINT RECTANGLE
	# = = = = = = = = = = = = = = = =
	# myrect = Rectangle(-200.0, -100.0, 200.0, 150.0, 'blue', 2, 'red')
	# draw_rectangle(canv, myrect)

	# DRAWING POINT
	# = = = = = = = = = = =  = = = =
	# point - is just a Rectangle baby!
	# we would not use             x2 ,  y2
	# mypoint = Rectangle(0.0, 50.0, 0.0, 0.0, 'blue', 2, 'blue')
	# draw_point(canv, mypoint)

	# DRAWING CIRCLE
	# = = = = = =  = = = = = = = = =
	# mycircle = Circle(50.0, 50.0, 70, 'blue', 5, 'red')
	# draw_circle(canv, mycircle)

	# DRAWING CZ FLAG
	# = = = = = = = = = = = = = = = =
	cz_flag(canv)

	world.mainloop()
