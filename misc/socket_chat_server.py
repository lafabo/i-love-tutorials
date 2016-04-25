#!/usr/bin/env python
# -*- coding: utf-8 -*-
from socket import *
from select import *

# setting
host = '127.0.0.1'
port = 8880

server = socket(AF_INET, SOCK_STREAM)
server.bind((host, port))
server.listen(5)

clients = []


def get_clients():
	use = []
	for client in clients:
		use.append(client[0])
	return use


def main_loop():
	while True:
		read, write, error = select([server], [], [], 0)

		if len(read):
			client, address = server.accept()
			clients.append([client, address, []])

		use = get_clients()

		try:
			read, write, error = select(use, [], [], 0)
			if len(read):
				for client in read:
					data = client.recv(1024)
					print(bytes.decode(data))
					if data == 0:
						for c in clients:
							if c[0] == client:
								clients.remove(c)
								break
					else:
						for c in clients:
							c[2].append(data)
		except:
			print 'An error! Hurray!'


		try:
			use = get_clients()
			read, write, error = select([], use, [], 0)

			if len(write):
				for client in write:
					for c in clients:
						if c[0] == client:
							for data in c[2]:
								sent = client.send(data)
								if sent == len(data):
									c[2].remove(data)
							break
		except:
			print('An error! Hiphip!')


if __name__ == '__main__':
	main_loop()
