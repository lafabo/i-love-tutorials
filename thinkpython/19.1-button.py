#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Gui import *

gu = Gui()
gu.title('Titletitletitle')
gu.la(text='Press the bt 1')


def create_button():
	gu.bu(text='bt 2', command=change_label)


def change_label():
	gu.la(text='Label')


gu.bu(text='bt 1', command=create_button)
gu.mainloop()

