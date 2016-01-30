def eval_loop():
	result = None
	while True:
		line = input("Print here whatever you want to interpretate with Python: ")
		if line == 'done':
			break
		result = eval(line)
		print result
	return result

eval_loop()