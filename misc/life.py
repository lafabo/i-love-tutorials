#!/usr/bin/env python
# -*- coding: utf-8 -*-
# most part by https://habrahabr.ru/company/mailru/blog/228379/

from Tkinter import Tk, Canvas, Button, Frame, BOTH, NORMAL, HIDDEN


def refresh():
	for i in range(field_height):
		for j in range(field_width):
			k = 0
			for i_shift in range(-1, 2):
				for j_shift in range(-1, 2):
					if canvas.gettags(cell_matrix[addr(i + i_shift, j + j_shift)])[0] == 'vis' and (
							i_shift != 0 or j_shift != 0):
						k += 1
			current_tag = canvas.gettags(cell_matrix[addr(i, j)])[0]
			if k == 3:
				canvas.itemconfig(cell_matrix[addr(i, j)], tags=(current_tag, 'to_vis'))
			if k == 4:
				canvas.itemconfig(cell_matrix[addr(i, j)], tags=(current_tag, 'to_hid'))
			if k == 2 and canvas.gettags(cell_matrix[addr(i, j)])[0] == 'vis':
				canvas.itemconfig(cell_matrix[addr(i, j)], tags=(current_tag, 'to_vis'))


def repaint():
	for i in range(field_height):
		for j in range(field_width):
			if canvas.gettags(cell_matrix[addr(i, j)])[1] == 'to_hid':
				canvas.itemconfig(cell_matrix[addr(i, j)], state=HIDDEN, tags=('hid', '0'))

			if canvas.gettags(cell_matrix[addr(i, j)])[1] == 'to_vis':
				canvas.itemconfig(cell_matrix[addr(i, j)], state=NORMAL, tags=('vis', '0'))


def step():
	refresh()
	repaint()


def draw_a(e):
	ii = (e.y - 3) / cell_size
	jj = (e.x - 3) / cell_size
	canvas.itemconfig(cell_matrix[addr(ii, jj)], state=NORMAL, tags='vis')


def addr(ii, jj):
	if ii < 0 or jj < 0 or ii >= field_height or jj >= field_width:
		return len(cell_matrix) - 1
	else:
		return ii * (w / cell_size) + jj


def clear():
	for i in range(field_height):
		for j in range(field_width):
			canvas.itemconfig(cell_matrix[addr(i, j)], state=HIDDEN, tags=('hid','0'))


if __name__ == '__main__':
	root = Tk()
	w = 350
	h = 370
	# window size
	root.geometry('%sx%s' % (w, h+30))
	cell_size = 20

	canvas = Canvas(root, height=h)
	canvas.pack(fill=BOTH)

	field_height = h / cell_size
	field_width = w / cell_size

	cell_matrix = []
	for i in range(field_height):
		for j in range(field_width):
			square = canvas.create_rectangle(2 + cell_size * j,
			                                 2 + cell_size * i,
			                                 cell_size + cell_size * j - 2,
			                                 cell_size + cell_size * i - 2,
			                                 fill="green")

			canvas.itemconfigure(square, state=HIDDEN, tags=('hid', '0'))
			cell_matrix.append(square)

	fict_square = canvas.create_rectangle(0, 0, 0, 0, state=HIDDEN, tags=('hid', '0'))

	cell_matrix.append(fict_square)

	frame = Frame(root)
	bt1 = Button(frame, text='Eval', command=step)
	bt2 = Button(frame, text='Clear', command=clear)

	bt1.pack(side='left')
	bt2.pack(side='right')

	frame.pack(side='bottom')

	canvas.bind('<B1-Motion>', draw_a)
	canvas.bind('<ButtonPress>', draw_a)

	root.mainloop()
