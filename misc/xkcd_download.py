#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import os


def find_pic(url):
	try:
		if requests.request('GET', url) is not None:
			soup = BeautifulSoup(requests.request('GET', url).read())
			imgurl = 'http' + soup.img.get('src')
			filename = './xkcd' + url.split('/')[1]

	except:
		exit('Sorry, not this time')


if __name__ == '__main__':
	pass