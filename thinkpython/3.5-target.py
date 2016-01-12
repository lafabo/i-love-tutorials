def draw():
	for i in range(11):
		for j in range(11):
			if i in [0, 5, 10] and j in [0, 5, 10]:
				print "+",
			elif i in [0, 5, 10] and j not in [0, 5, 10]:
				print "-",
			elif j in [0, 5, 10] and i not in [0, 5, 10]:
				print "|",
			else:
				print " ",
		print ''



def draw2(size, raws):
	part = (size+1) / (raws-1)
	step = range(0, size+1, part)

	for i in range(size+1):
		for j in range(size+1):
			if i in step and j in step:
				print "+",
			elif i in step and j not in step:
				print "-",
			elif j in step and i not in step:
				print "|",
			else:
				print " ",
		print ''



draw()

draw2(20, 5)