from datetime import datetime, timedelta

starttime = '6:52:00'.split(":")

a = datetime(year=2016, month=1, day=12, hour=int(starttime[0]), minute=int(starttime[1]), second=int(starttime[2]))

first_mile_t = '0:08:15'
first_dist = 1
second_mile_t = '0:07:12'
second_dist = 3
third_mile_t = '0:08:15'
third_dist = 1

def time_to_sec(time):
	h, m, s = time.split(':')
	sec = int(s) + int(m)*60 + int(h)*3600
	return sec


# standard library rules!
run_time = first_dist * time_to_sec(first_mile_t) + second_dist * time_to_sec(second_mile_t) + third_dist * time_to_sec(third_mile_t)

print str(a + timedelta(seconds=run_time))