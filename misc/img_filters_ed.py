#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw
from sys import argv
from random import randint


sepia_depth = 30


def grayscale(image):
	for i in range(image.width):
		for j in range(image.height):
			a = image.pix[i, j][0]
			b = image.pix[i, j][1]
			c = image.pix[i, j][2]
			S = (a + b + c) // 3
			image.draw.point((i, j), (S, S, S))


def sepia(image, sepia_depth):
	for i in range(image.width):
		for j in range(image.height):
			a = image.pix[i, j][0]
			b = image.pix[i, j][1]
			c = image.pix[i, j][2]
			S = (a + b + c) // 3
			a = S + sepia_depth * 2
			b = S + sepia_depth
			c = S
			if a > 255: a = 255
			if b > 255: b = 255
			if c > 255: c = 255
			image.draw.point((i, j), (a, b, c))


def negative(image):
	for i in range(image.width):
		for j in range(image.height):
			a = image.pix[i, j][0]
			b = image.pix[i, j][1]
			c = image.pix[i, j][2]
			image.draw.point((i, j), (255-a, 255-b, 255-c))


def blackandwhite(image, factor=100):
	for i in range(image.width):
		for j in range(image.height):
			a = image.pix[i, j][0]
			b = image.pix[i, j][1]
			c = image.pix[i, j][2]
			S = a + b + c
			if S > (((255 + factor) // 2) * 3):
				a, b, c = 255, 255, 255
			else:
				a, b, c = 0, 0, 0
			image.draw.point((i, j), (a, b, c))


def brightness(image, factor=20):
	for i in range(image.width):
		for j in range(image.height):
			a = image.pix[i, j][0] + factor
			b = image.pix[i, j][1] + factor
			c = image.pix[i, j][2] + factor
			if a < 0: a = 0
			if b < 0: b = 0
			if c < 0: c = 0

			if a > 255: a = 255
			if b > 255: b = 255
			if c > 255: c = 255
			image.draw.point((i, j), (a, b, c))


def noize(image, factor=5):
	for i in range(image.width):
		for j in range(image.height):
			rand = randint(-factor, factor)
			a = image.pix[i, j][0] + rand
			b = image.pix[i, j][1] + rand
			c = image.pix[i, j][2] + rand
			if a < 0: a = 0
			if b < 0: b = 0
			if c < 0: c = 0

			if a > 255: a = 255
			if b > 255: b = 255
			if c > 255: c = 255
			image.draw.point((i, j), (a, b, c))


def contrast(image, factor):
	pass


if __name__ == '__main__':

	working_image = MyImage()

	working_image.image = Image.open(argv[1])
	working_image.draw = ImageDraw.Draw(working_image.image)
	working_image.width = working_image.image.size[0]
	working_image.height = working_image.image.size[1]
	working_image.pix = working_image.image.load()

	working_image.image.save('output.jpg', 'JPEG')
	del working_image.draw