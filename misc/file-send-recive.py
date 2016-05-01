#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import socket

import sys

port = 8080
host = 'localhost'


# server side
def send_file(path):
	with open(path, 'wb') as f:
		while True:
			c, addr = s.accept()
			l = c.recv(1024)
			while l:
				f.write(l)
				l = c.recv(1024)
				print('.',)
			print('\nRecived')


# client side
def get_file(path):
	s.connect((host, port))
	with open(path, 'rb') as f:
		l = f.read(1024)
		while l:
			s.send(l)
			l = f.read(1024)
		print('Done')
		s.shutdown(socket.SHUT_WR)
		print(s.recv(1024))


if __name__ == '__main__':
	s = socket.socket()
	s.bind(host, port)
	s.listen(3)
