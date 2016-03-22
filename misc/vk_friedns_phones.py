#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by https://habrahabr.ru/post/279803/ tutorial
import vk
from time import sleep
from re import sub, findall
from getpass import getpass
from csv import writer, QUOTE_ALL


class User(object):
	def __init__(self, login, password):
		self.login = login
		self.password = password
		self.id = ''

	# можно в лёгкую объеденить __инит__ и аутх и хранить api в классе
	# потом обязательно сделаю todo
	def auth(self):
		session = vk.AuthSession(app_id='5340228', user_login=self.login, user_password=self.password)
		api = vk.API(session)
		return api

	def friends(self, api):
		userfriends = api.friends.get(user_id=self.id, order='hints')
		return userfriends

	def friends_count(self, api):
		user_friends = User.friends(self, api)
		friends_count = len(user_friends)
		return friends_count

	def info(self, api):
		user = api.users.get(user_id=self.id)
		return user[0]

#############################################################
def check_number(str):
	if len(str) != '':
		norm = sub(r'(\s+)?[+]?[-]?', '', str)
		right = findall(r'[\d', norm)
		if len(right) == len(norm) and len(norm) >= 10:
			rev_norm = norm[::-1]
			norm = rev_norm[0:10]
			if norm[::-1][0] == '0':
				return norm
	else:
		return False


def find_correct_phones(api, friends, friends_count):
	user_phones = []
	for i in range(0, friends_count):
		cur_user_id = int(friends[i])
		cur_user = api.users.get(user_id=cur_user_id, fields='contacts')
		try:
			cur_mob = cur_user[0]['mobile_phone']
		except KeyError:
			sleep(0.3)
			continue
		mob = norm_mob(cur_mob)
		if mob:
			user_phones.append({
				'user_name': '%s %s' % (cur_user[0]['first_name'], cur_user[0]['last_name']),
				'user_phone': '8%s' % mob
			})

		sleep(0.4)

	return user_phones


def save_csv(data, path):
	with open(path, 'w') as csvfile:
		my_writer = writer(csvfile, delimiter=' ', quotechar='"', quoting=QUOTE_ALL)
		my_writer.writerow(('user_name', 'user_phone'))
		for item in data:
			try:
				my_writer.writerow((item['user_name'], item['user_phone']))
			except Exception:
				my_writer.writerow(('Encoding error', item['user_phone']))


class Timer(object):
	def __enter__(self):
		self.startTime = time()

	def __exit__(self, exc_type, exc_val, exc_tb):
		how_long = time() - self.startTime
		print('In %s min' % (how_long/60))





if __name__ == '__main__':
	while True:
		login = input('E-mail: ')
		password = input('Password: ')
		try:
			vk_user = User(login, password)
			api = vk_user.auth()
			print('Autorized')
			break
		except Exception:
			print('Wrong login/pass')

	friends = vk_user.friends(api)
	friends_count = vk_user.friends_count(api)
	print('Found %s friends' % friends_count)
	with Timer() as p:
		users_phones = find_correct_phones(api, friends, friends_count)

	save_csv(users_phones, 'vk.csv')
	print('Data saved')
