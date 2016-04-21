#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests, re, sys
from subprocess import Popen
def get_download_link(url):
	request = requests.get(url)
	program = re.compile('http://download.ted.com/talks/[^\"]*480p-en.mp4')
	return program.findall(request.text)[-1]


def create_download_list(soup):
	talk = []
	for vid in soup.findall('a', {'class':'playlist-talks__play'}, href=True):
		talk.append(vid)
	return talk


def download(url):
	complete_url = "http://www.ted.com" + url
	download_link = get_download_link(complete_url)
	download_name = download_link[download_link.rfind("/")+1:]
	Popen('wget -c -O \"%s\" \"%s\"\n' % (download_name, download_link))


if __name__ == '__main__':
	r = requests.get(sys.argv[1])
	soup = BeautifulSoup(r.text)
	for item in create_download_list(soup)
		download(item)

# this should work!