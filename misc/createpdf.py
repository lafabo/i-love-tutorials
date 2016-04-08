#!/usr/bin/env python
# -*- coding: utf-8 -*-
from reportlab.pdfgen import canvas

def hello(str):
	c = canvas.Canvas('hello.pdf')
	c.drawString(100, 100, str)
	c.showPage()
	c.save()

hello('Whosyourdaddy')
