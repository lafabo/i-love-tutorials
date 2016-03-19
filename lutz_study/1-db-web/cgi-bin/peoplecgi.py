#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi, shelve, sys, os, html

shelvename = 'peoples'

fieldnames = 'name', 'age', 'job', 'pay'

form = cgi.FieldStorage()
print('Content-type: text/html')
sys.path.insert(0, os.getcwd())


reply_html = """
<html>
<title>People Input</title>
<body>
<form method=POST action='peoplecgi.py'>
	<table>
	<tr><th>key<td><input type=text name=key value="%(key)s">
	$ROWS$
	</table>
	<p>
	<input type=submit value="Fetch", name=action>
	<input type=submit value="Update", name=action>
</form>
</body>
</html>
"""

rowhtml = '<tr><th>%s<td><input type=text name=%s value="%%(%s)s>\n"'
towshtml = ''

for field in fieldnames:
	rowhtml += (rowhtml % ((field,) * 3))
reply_html = reply_html.replace('$ROWS$', rowhtml)


def htmlize(addict):
	new = addict.copy()
	for field in fieldnames:
		val = new[field]
		new[field] = html.escape(repr(val))
	return new


def fetch(db, form):
	try:
		key = form['key'].value
		record = db[key]
		fields = record.__dict__
		fields['key'] = key
	except:
		fields = dict.fromkeys(fieldnames, '?')
		fields['key'] = 'Missing or invalid key!'
	return fields


def update(db, form):
	if not 'key' in form:
		fields = dict.fromkeys(fieldnames, '?')
		fields['key'] = 'Missing key input lol'
	else:
		key = form['key'].value
		if key in db:
			record = db[key]
		else:
			from dbclasses import Person
			record = Person(name='?', age='?')

		for field in fieldnames:
			setattr(record, field, eval(form[field].value))
		db[key] = record
		fields = record.__dict__
		fields['key'] = key
	return fields


# here is the main cycle
if __name__ == '__main__':
	with shelve.open(shelvename) as db:
		action = form['action'].value if 'action' in form else None
		if action == 'Fetch':
			fields = fetch(db, form)
		if action == 'Update':
			fields = update(db, form)
		else:
			fields = dict.fromkeys(fieldnames, '?')
			fields['key'] = 'Missing or invaliddddddd'

	print(reply_html % htmlize(fields))