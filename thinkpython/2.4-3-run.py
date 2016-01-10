starttime = '6:52:00'

first_mile_t = '0:08:15'
first_dist = 1
second_mile_t = '0:07:12'
second_dist = 3
third_mile_t = first_mile_t
third_dist = 1

def time_to_sec(time):
	h, m, s = time.split(':')
	sec = int(s) + int(m)*60 + int(h)*3600
	return sec

def dist_to_time(sec, dist):
	return dist * sec

def sec_to_time(sec):
	h = sec // 3600
	m = (sec - sec // 3600) // 60
	s = (h*3600 + m*60) - sec
	return h, m, s


def addclock(time):
	h = time[0]
	m = time[1]
	s = time[2]

	h_add = s % 3600
	s -= s % 3600

	m_add = s % 60
	s -= s % 60

	h_add += m % 60
	m -= m % 60

	h += h_add
	m += m_add

	return h % 3600, m % 3600, s % 3600


current_time = sec_to_time(time_to_sec(starttime) +
                  dist_to_time(time_to_sec(first_mile_t),first_dist) +
                  dist_to_time(time_to_sec(second_mile_t), second_dist) +
                  dist_to_time(time_to_sec(third_mile_t), third_dist))

print addclock(current_time)