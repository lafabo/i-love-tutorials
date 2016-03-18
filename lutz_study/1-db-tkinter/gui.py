#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.messagebox import showerror
from dbclasses import Person
import shelve

shelvename = 'peoples'
fieldnames = 'name', 'age', 'job', 'pay'


def wigets():
	global entries

	window = Tk()
	window.title('People Shelve')
	form = Frame(window)
	form.pack()

	entries = {}
	for ix, label in enumerate(('key', ) + fieldnames):
		lab = Label(form, text=label)
		ent = Entry(form)
		lab.grid(row=ix, column=0)
		ent.grid(row=ix, column=1)
		entries[label] = ent

	Button(window, text='Get', command=fetch).pack(side=LEFT)
	Button(window, text='Update', command=update).pack(side=LEFT)
	Button(window, text='Quit', command=window.quit()).pack(side=RIGHT)

	return window


def fetch():
	key = entries['key'].get()
	try:
		record = db[key]
	except:
		showerror(title='Error', message='No suck key!')
	else:
		for field in fieldnames:
			entries[field].delete(0, END)
			entries[field].insert(0, repr(getattr(record, field)))


def update():
	key = entries['key'].get()
	if key in db:
		record = db[key]
	else:
		record = Person(name='?', age='?')

	for field in fieldnames:
		setattr(record, field, eval(entries[field].get()))

	db[key] = record


if __name__ == '__main__':
	db = shelve.open(shelvename)
	window = wigets()
	window.mainloop()
	db.close()
