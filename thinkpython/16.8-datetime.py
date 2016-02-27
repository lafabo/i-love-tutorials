#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime


today = datetime.datetime.now()

days = {
	0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
    }


def get_next_birthday(fromdate):
	bdate_year = datetime.datetime(1988, 3, 4)
	#datetime.timedelta()

	age = fromdate.year - bdate_year.year       # only years, not days month
	return age


def to_next_bday(fromday, bday):
	if fromday.year < bday.year:
		bday = bday.replace(year=today.year + 1)

	days_to_bday = abs(fromday - bday)
	return days_to_bday

if __name__ == '__main__':
	print days[today.weekday()]
	print get_next_birthday(today)
	print to_next_bday(today, datetime.datetime(2016, 3, 4))
