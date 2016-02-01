momstart = 73-37
sonstrat = 0

for i in range(0, 99):
	if str(momstart+i) == str(sonstrat+i)[::-1]:
		print momstart+i, sonstrat+i
