#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Tkinter
from swampy import Gui

def change_label():
	g.la(text='Thanks')

if __name__ == '__main__':
	g = Gui()
	g.title('Gugugugui!')
	button = g.bu(text='Press x to win')
	label = g.la(text='Push the tempo')

	button2 = g.bu(text='Push the tempo', command=change_label())
	g.mainloop()
