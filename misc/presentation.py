#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import random
import socket
import BaseHTTPServer
import re

handler_class = BaseHTTPServer.BaseHTTPRequestHandler
token = '/%s/' % random.randint(0, sys.maxint)
page = 1
validate = re.compile(token + '(prev|next)$')


def send_key(key):
	os.system("FvwmCommand 'All (VCLSalFrame) FakeKeypress press {}'".format(key))


class Hanbler(BaseHTTPServer.BaseHTTPRequestHandler):
	def link(self, s, n):
		if n < 0 or n >= len(data):
			return ' '
		return '<a href="%s%s">%s</a>' % (token, s, s)

	def do_get(self):
		cmd = validate.match(self.path)
		if cmd is None:
			self.send_response(404)
			self.send_header("Content-type", "text/html")
			self.end_headers()
			self.wfile.write('<h1>OK</h1>')
			return

		global page

		if cmd.group(1) == 'prev' and page > 0:
			page -= 1
			send_key('BackSpace')

		elif cmd.group(1) == 'next' and page < len(data) - 1:
			page += 1
			send_key('Space')

		self.send_response(200)
		self.send_header('Content-type', 'text/html; charset=utf-8')
		self.end_headers()
		self.wfile.write("""
		{pagenum} - {next}
		<hr> {data} </hr>
		{prev} - {pagenum}
		""".format(prev = self.link('prev', page - 1), pagenum = page + 1,
		           next = self.link('next', page + 1), data = data[page]))


def read_file(s):
	with open(s) as f:
		return re.split('--- *\n?', f.read())



if __name__ == '__main__':
	pass