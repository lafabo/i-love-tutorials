# -*- coding: utf-8 -*-

string = unicode('Joann loves pizza as much as Борис - vodka. Ja, Vodka!', 'UTF-8')

encodinglist = ['UTF-8', 'UTF-16', 'UTF-32', 'CP1251', 'CP866', 'ASCII', 'ISO-8859-5']

for i in encodinglist:
	print i, ': ', string.encode(i, errors="ignore")