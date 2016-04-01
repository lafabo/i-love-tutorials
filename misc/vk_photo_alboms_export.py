#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import datetime
from getpass import getpass
import os
import time
import sys
import requests

try:
	from vk_api import VkApi
except ImportError:
	print("Error importing vk_api")
	sys.exit(0)


def connect(login, password):
	return VkApi(login, password)


def get_albums(connection):
	return connection.method('photos.getAlbums')


def get_photos(connection, album_id):
	return connection.method('photos.get', {'aid': album_id})


def download(photo, output):
	url = photo.get('src_xxxbig') or photo.get('src_xxbig') or \
	      photo.get('src_xbig') or photo.get('src_big')

	r = requests.get(url)
	title = photo['pid']
	with open(os.path.join(output, '%s.jpg' % title), 'wb') as f:
		for buf in r.iter_content(1024):
			if buf:
				f.write(buf)


def sizeof_fmt(num):
	for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
		if num < 1024.0:
			return '%3.1f %s' % (num, x)
		num /= 1024.0


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='', version='%s' )
	parser.add_argument('username')
	#
	args = parser.parse_args()

	if args.output.startwith('~'):
		args.output = os.path.expanduser(args.output)

	start_time = datetime.datetime.now()
	try:
		password = getpass('Password: ')
		connection = connect(args.username, password)

		albums = get_albums(connection)
		print('Found %s' % len(albums))

		ix = 0
		for album in albums:
			print('%sd. %-40s %4s item(s)' % (ix+1,  album['title'], album['size']))
			ix += 1

		time.sleep(1)

		if not os.path.exists(args.output):
			os.makedirs(args.output)

		for album in albums:
			response = get_photos(connection, album['aid'])
			output = os.path.join(args.output, album['title'])
			if not os.path.exists(output):
				os.makedirs(args.output)

			processed = 0

			for photo in response:
				percent = round(float(processed) / float(len(response)) * 100, 2)
				sys.stdout.flush()

				download(photo, output)
				processed += 1

	finally:
		print('Done in %s' % (datetime.datetime.now()-start_time))
