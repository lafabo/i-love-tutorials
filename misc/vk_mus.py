#!/usr/bin/env python
# -*- coding: utf-8 -*-
from urllib.request import urlopen
import json

user_id = ''
token = ''


address = 'https://api.vk.com/method/audio.get?owner_id=%s&access_token=%s' % (user_id, token)
data = urlopen(address)
response = json.loads(data.read().decode())
songs = response['response'][1:]

for song in songs:
	artist = song['artist']
	title = song['title']
	url = song['url']

	cashed_song = urlopen(url).read()
	path = 'Music/%s/%s.mp3' % (artist, title)

	with open(path, 'wb') as mp3file:
		mp3file.write(cashed_song)



