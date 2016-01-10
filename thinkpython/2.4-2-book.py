price = 24.95
discont = 0.4
delivery = 3
delivery_2 = 0.75

num = int(raw_input("Enter how many books you want to buy: "))

if num > 1:
	summ = price + delivery + (num-1)*(price*discont) + (num-1)*delivery_2
	print summ
elif num == 1:
	summ = price + delivery
	print summ
else:
	print 'Something wrong'
	exit(1)
