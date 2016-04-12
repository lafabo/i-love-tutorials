#!/usr/bin/env python
# -*- coding: utf-8 -*-
from hashlib import md5
from PIL import Image, ImageDraw, ImageFont
import random
from StringIO import StringIO


def generate_captcha(request):
    path = '.'
    im = Image.new('RGBA', (200, 50), (0, 0, 0, 0))
    draw = ImageDraw(im)
    number = ''
    margin_left, margin_top = 0, 0
    colnum = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    i = 0
    while i < 6:
        font_color = '#' + str(random.randint(0,9))
        y = 0
        while y < 5:
            rand = random.choice(colnum)
            font_color = font_color + rand
            y += 1
        rand_x11 = random.randint(0, 100)
        rand_x12 = random.randint(100, 200)
        rand_y11 = random.randint(0, 50)
        rand_y12 = random.randint(0, 50)
        draw.line((rand_x11, rand_y11, rand_x12, rand_y12), fill='#a9a6a6')
        font_rand = str(random.randint(1, 10))
        font_size_rand = random.randint(30, 40)
        font = ImageFont.truetype(path + "fonts/" + font_rand + ".ttf", font_size_rand)
        a = str(random.randint(0, 9))
        draw.text((margin_left, margin_top), a, fill=str(font_color), font=font)
        rand_x11 = random.randint(0, 100)
        rand_x12 = random.randint(100, 200)
        rand_y11 = random.randint(0, 50)
        rand_y12 = random.randint(0, 50)
        draw.line((rand_x11, rand_y11, rand_x12, rand_y12), fill="#a9a6a6")
        margin_left = margin_left + random.randint(20, 35)
        margin_top = random.randint(0, 20)
        i += 1
        number += a
    salt = "$@!SAf*$@)ASFfacnq==124-2542SFDQ!@$1512czvaRV"
    key = md5(str(number + salt)).hexdigest()
    output = StringIO()
    im.save(output, format="PNG")
    contents = output.getvalue().encode("base64").replace("\n", "")
    img_tag = '<img value="' + key + '" src="data:image/png;base64,{0}">'.format(contents)
    output.close()
    return img_tag



if __name__ == '__main__':
    pass
