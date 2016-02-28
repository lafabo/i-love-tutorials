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
    6: 'Sunday'}


def days_bday(fromday, bday):
	if fromday.year < bday.year:
		bday = bday.replace(year=today.year + 1)

	days_to_bday = abs(fromday - bday)
	return days_to_bday


if __name__ == '__main__':
	print days[today.weekday()]
	print days_bday(today, datetime.datetime(2016, 3, 4))
