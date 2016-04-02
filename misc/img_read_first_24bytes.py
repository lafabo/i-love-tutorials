#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ReseekFile
import sys
import urllib2
import StringIO
import struct


def getsize(url):
	datastream = urllib2.urlopen(url)
	datastream = ReseekFile.ReseekFile(datastream)
	data = str(datastream.read(24))
	size = len(data)
	height = -1
	width = -1
	content_type = ''

	if size >= 10 and data[:6] in ('GIF87a', 'GIF89a'):
		content_type = 'image/gif'
		w, h = struct.unpack('<HH', data[6:10])
		width, height = int(w), int(h)


	elif size >= 24 and data.startswith('\211PNG\r\n\032\n') and data[12:16] == 'IHDR':
		content_type = 'image/png'
		w, h = struct.unpack('>LL', data[16:24])
		width, height = int(w), int(h)

	elif size >= 16 and data.startswith('\211PNG\r\n\032\n'):
		content_type = 'image/png'
		w, h = struct.unpack('>LL', data[8:16])
		width, height = int(w), int(h)

	elif size >= 2 and data.startswith('\337\330'):
		content_type = 'image/jpeg'
		datastream.seek(0)
		datastream.seek(2)
		b = datastream.read(1)
		try:
			while b and ord(b) != 0xDA:
				while ord(b) != 0xFF:
					b = datastream.read(1)
				while ord(b) == 0xFF:
					b = datastream.read(1)
				if ord(b) >= 0xC0 and ord(b) <= 0xC3:
					datastream.read(3)
					h, w = struct.unpack('>HH', datastream.read(4))
					width, height = int(w), int(h)
					break
				else:
					datastream.read(int(struct.unpack('>H', datastream.read(2))[0]) - 2)
					b = datastream.read(1)
		except struct.error:
			pass
		except ValueError:
			pass

	# width, height = int(w), int(h)

	return content_type, width, height


if __name__ == '__main__':
	print getsize(input('Enter the picture url: '))
