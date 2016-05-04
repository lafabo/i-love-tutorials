#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os.path import isfile
import vk_api

def check_source(argv):
	# vk post
	if argv.startswith('https://vk.com/wall-'):
		parse_from_vk(argv)
	# file
	elif isfile(argv):
		parse_from_file(argv)
	else:
		raise ValueError('Sorry, only vk posts and txt files')


def parse_books_from_list(booklist):
	# here would be re for author - "book", 'book' - author, and etc
	# return all text
	pass


def parse_from_vk(link):
	# vk access by .... SCRAPPING!

	login, password = 'python@vk.com', 'mypassword'
	vk_session = vk_api.VkApi(login, password)

	try:
		vk_session.authorization()
	except:
		vk_api.AuthorizationError():
		exit(0)

	tools = vk_api.VkTools(vk_session)

	wall = tools.get_all('wall.get', )


def parse_from_file(filepath):
	with open(filepath, 'r') as f:
		return f.readall()


def download_book(author_book):
	# beautiful soup + request
	# chose format .moby , .epub, etc
	pass


def downloaded_to_zip(files):
	pass


if __name__ == '__main__':
	# $ python3 scriptname.py 'link to vk' or 'file with authors-books'
	pass
