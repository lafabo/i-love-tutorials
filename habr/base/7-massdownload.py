# -*- coding: utf-8 -*-
'''
— Разработать программу «массовой закачки» URL-ов из файла urls.txt
'''
import urllib, os

urls = open('urls.txt', 'r')

for url in urls.readlines():

	if url != '':

		remotefile = urllib.urlopen(url)
		filename = '7-tmp/' + os.path.basename(url)
		savefile = open(filename, 'w')

		for line in remotefile:
			savefile.write(line)

		savefile.close()

urls.close()

