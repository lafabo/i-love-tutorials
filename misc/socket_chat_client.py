#!/usr/bin/env python
# -*- coding: utf-8 -*-
from socket import *
from select import *

host = '127.0.0.1'
port = 8880

sock = socket(AF_INET, SOCK_STREAM)
sock.connect((host, port))


def main_loop():
	data = input("&gt;&gt; ")
	read, write, error = select([], [sock], [], 0)
	if len(write):
		b = sock.send(str.encode(data))

	# receive
	while True:
		read, write, error = select([sock], [], [], 1)

		if len(read):
			data = bytes.decode(sock.recv(1024))
			print(data)
		else:
			break


if __name__ == '__main__':
	main_loop()
