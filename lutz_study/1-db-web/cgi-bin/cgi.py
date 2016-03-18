#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi, html

form = cgi.FieldStorage()
print('Content-type: text/html\n')
print('<title>Reply page</title>')

if not 'user' in form:
	print('<h1>Who are you?</h1>')
else:
	print('<h1>Hello, <i>%s</i>!</h1>' % form['user'].value)
