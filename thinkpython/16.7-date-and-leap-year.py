#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Date(object):
	"""
	day month year
	"""


def increment_date(date, ndays):
	"""
	# set up if month is february
	if year % 4 == 0:
		avalable_days = 28
	else:
		avalable_days = 29

	if date.m in (1, 3, 5, 7, 8, 10, 12):
		avalable_days = 31
	elif date.m in (4, 9, 11):
		avalable_days = 30
	"""
	"""
	Как мне кажется, проще всего переводить дни в номер дня в году, прибавлять и смотреть
	if today + days > 365:
	 year ++
	elif today + days < 365
	 year = year
	 m, d = divmod(today + days, 30) ----- вот тут имеет смысл использовать табличку выше,
	 что бы узнать сколько в месяце текущем - дней
	"""





def is_year_leap(date):
	pass


def increase_day():
	pass


def increase_month():
	pass


def increase_year():
	pass


if __name__ == '__main__':
	d = Date()
	d.d = 1
	d.m = 12
	d.y = 2015

