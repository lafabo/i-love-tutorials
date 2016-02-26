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
	bdate_year = datetime.datetime.year

	age = today.year - bdate_year




if __name__ == '__main__':
	print days[today.weekday()]