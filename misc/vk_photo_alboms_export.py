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


def main_cycle():


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='', version='%s' )
	parser.add_argument('username')
	#
	args = parser.parse_args()

	if args.output.star