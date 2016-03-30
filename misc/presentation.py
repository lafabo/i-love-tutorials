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


def ip():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(('192.168.1.1', 0))                           # here is our server setting
	return s.getsockname()[0]


def make_url(port):
	url = 'http://%s:%s%sprev' % (ip(), port, token)
	print url
	os.system('firefox "http://chart.apis.google.com/chart?cht=qr&chs=200x200&chl=%s"' % url)


def run():
	for port in random.sample(xrange(8000, 9000), 1000):
		try:
			httpd = BaseHTTPServer.HTTPServer(('', port), Hanbler)
			httpd.server_activate()
			make_url(port)
			httpd.serve_forever()
		except socket.error, e:
			if e.errno not in (98, ):
				print e
				exit()
		except KeyboardInterrupt:
			print('\n\nExiting')
			exit()


if __name__ == '__main__':
	data = read_file('notes.txt')
	print('Got %s slides' % len(data))
	run()
