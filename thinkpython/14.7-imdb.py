#!/usr/bin/env python
# -*- coding: utf-8 -*-
import imdb
import shelve
from collections import defaultdict


def print_info(actor, date, title, role):
	return actor, date, title, role


def to_the_list(actor, date, title, role):
	all_genders.append((actor, date, title, role))
	# return a [(actor, date, title, role), ]


def db_actor_film(actor, date, title, role):
	act_film = defaultdict(list)
	for i in all_genders:
		act_film[i[0]].append(i[2])

	return act_film
	# shelve.open('imdb.db', 'c')
	# return { actor : [list, of, his, films] }


def db_film_actor(actor, date, title, role):
	act_act = defaultdict(list)
	for i in all_genders:
		act_act[i[2]].append(i[0])
	return act_act
	# return { actor: [actor2, actor56]}


def db_actor_actor(actor, date, title, role):
	'''
	act_act = defaultdict(list)
	for i in all_genders:
		act_act[i[2]].append(i[0])
	'''
	pass


all_genders = []


def from_x_to_kevin(actor):
	pass
	# return tuple [x_actor -> other_actor -> .... -> kevin]


if __name__ == '__main__':
	print imdb.process_file('actors.list.gz', db_actor_film)

