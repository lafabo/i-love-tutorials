#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image
from images2gif import writeGif
import sys
from time import time


def create_gif(images):

	duration = 0.1 * len(images)
	giffile = str(time()) + '.gif'

	frames = []
	for frame in images:
		frames.append(Image.open(frame))

	writeGif(giffile, frames, duration)


if __name__ == '__main__':
	files = sys.argv[1:]
	create_gif(files)
