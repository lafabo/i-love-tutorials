#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import Image


def check_has_exif(img):
	pass


def save_without_exif(img):
	with Image.open(img, 'w') as image_file:
		data = list(image_file.getdata())

		with Image.new(image_file.mode, image_file.size) as image_without_exif:
			image_without_exif.putdata(data)
			image_without_exif.save(img)

filelist = []


def get_images_in_dir(path):
	for current_path in path:
		for (dir, _, files) in os.walk(current_path):
			for f in files:
				path = os.path.join(dir, f)
				if os.path.exists(path):
					if check_has_exif(path):
						filelist.append(path)

if __name__ == '__main__':
	pass