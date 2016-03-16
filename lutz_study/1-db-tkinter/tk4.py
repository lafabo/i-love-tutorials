#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from tk3 import MyGui

mainwin = Tk()
Label(mainwin, text=__name__).pack()

popup = Toplevel()
Label(popup, text='Attach').pack(side=LEFT)
MyGui(popup).pack(side=RIGHT)
mainwin.mainloop()