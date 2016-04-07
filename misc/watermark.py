#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont, ImageEnhace
import os, sys

font = '/albumgen/fonts/Comfortaa-Light.ttf'


def add_watermark(in_file, text, out_file='wm.jpg', angle=25, opacity=0.25):
	with Image.open(in_file).convert('RGB') as img:
		watermark = Image.new('RGBA', img.size, (0, 0, 0, 0))
		size = 2
		n_font = ImageFont.truetype(font, size)
		n_width, n_height = n_font.getsize(text)
		while n_width + n_height < watermark.size[0]:
			size += 2
			n_font = ImageFont.truetype(font, size)
			n_width, n_height = n_font.getsize(text)
		draw = ImageDraw.Draw(watermark, 'RGBA')
		draw.text((watermark.size[0] - n_width) / 2,
		          (watermark.size[1] - n_height) / 2,
		          text, font=n_font)
		watermark = watermark.rotate(angle, Image.BICUBIC)
		alpha = watermark.split()[3]
		alpha = ImageEnhace.Brightness(alpha).enhance(opacity)
		watermark.putalpha(alpha)
		Image.composite(watermark, img, watermark).save(out_file, 'JPEG')


if __name__ == '__main__':
	if len(sys.argv) < 3:
		sys.exit('Error')
	add_watermark(*sys.argv[1:])
