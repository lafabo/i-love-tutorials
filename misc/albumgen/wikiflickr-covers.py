#!/usr/bin/env python
#  -*- coding: utf-8 -*-
'''
Пилим обложки по рандомным данным

Название группы
http://en.wikipedia.org/wiki/Special:Random
http://ru.wikipedia.org/wiki/Служебная:Случайная_страница

Название альбома
http://en.wikiquote.org/wiki/Special:Random
http://ru.wikiquote.org/wiki/Служебная:Случайная_страница
(можно использовать кусок любой цитаты на странице)

Обложка
http://flickr.com/explore/interesting/7days (сохраняем страницу, потом из папки к ней выдираем, все просто)
http://photo.net/photodb/random-photo?category=NoNudes
https://commons.wikimedia.org/wiki/Special:Random/File

Но у меня нет шрифтов!
http://www.dafont.com/

В чем суть, спросишь ты? Все очень просто. Жмешь Random article на Википедии и Random page на Викицитатнике. Теперь картинка, которая тебе выпала - это обложка твоего музыкального альбома, название статьи на Википедии - название группы, а выпавшая цитата - название альбома. Далее расчехляешь пейнт, фотошоп или любой другой фоторедактор и скручиваешь все воедино.
Алсо, если цитат на странице много или они слишком длинные, можно вырвать любое предложение. Главное - не рероллить.

Постишь альбом, обсуждаешь с анончиками, пытаешься прикинуть стиль, в котором играет твоя вымышленная группа. Ну и так далее.
'''


import wikipedia, urllib, re, random, os
from PIL import ImageFont, Image, ImageDraw


#lang_list = ['ru', 'en', 'pl', 'uk', 'fr', 'cs'] # for more fun more languages

wikipedia.set_lang('ru')
group = wikipedia.random(pages=1)
album = wikipedia.random(pages=1)
cover = 'local-filename.jpg'

def getflickrphoto():

	url = "https://www.flickr.com/explore/interesting/7days"
	regex = '<img src="([^"]+)".*>'

	photolist = urllib.urlopen(url)
	raw_data = photolist.read()
	pattern = re.compile(regex)
	download = re.findall(pattern, raw_data)

	# first in download array is some yahoo statistics shit so we skip it
	x = random.randint(1, len(download))
	photo = download[x].replace('_m.', '_z.', 1)
	#photo = photo.replace('farm2.staticflickr.com/', 'c2.staticflickr.com/2')
	urllib.urlretrieve(photo, "local-filename.jpg")

	return "local-filename.jpg"


def printcover(group, album, cover):
	# let's chose random fonts
	album_font = ImageFont.truetype('/usr/share/fonts/dejavu/DejaVuSans.ttf', 45)
			#random.choice(os.listdir("/home/i/dev/i-love-tutorials/misc/albumgen/fonts")), 15)

	group_font = ImageFont.truetype('/usr/share/fonts/dejavu/DejaVuSans.ttf', 35)
	#print "\n\n\n\n\n", album_font, group_font

	# cover image
	cover_image = Image.open(cover)

	text_album_size = album_font.getsize(album)
	text_group_size = group_font.getsize(group)

	rand_color = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
	rand_color2 = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))

	draw = ImageDraw.Draw(cover_image)
	draw.text((10, 0), group, rand_color, font=group_font)
	draw.text((0, 200), album, rand_color2, font=album_font)


	cover_image.save('out.jpg')


if __name__ == '__main__':
	printcover(group, album, getflickrphoto())