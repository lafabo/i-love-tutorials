#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import mainloop
from tkinter.messagebox import showinfo
from tk3 import MyGui


class CustomGui(MyGui):
	def reply(self):
		showinfo(title='popup', message='ouch!')


if __name__ == '__main__':
	CustomGui().pack()
	mainloop()
