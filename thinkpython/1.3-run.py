# print help('print')

dist = float(raw_input("Enter the distance: "))
time = str(raw_input("Enter the time (only M:S format allowed): "))

def time_to_sec(time):
	m, s = time.split(':')
	seconds = int(m)*60 + int(s)
	return seconds

print 'You ran with speed: ', round(dist/(time_to_sec(time)/60), 2), 'km per minute'