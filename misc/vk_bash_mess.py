#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import json
import urllib2
import vk_auth

app_id = '4925055'
login = input(u"Enter your login: ")
password = input(u"Enter your pass: ")

url_dialog = "https://api.vk.com/method/messages.getHistory?count=20&user_id=%s&access_token=%s&v=5.33"


class Connect:
	def __init__(self, app_id, login, password):
		self.access_token = vk_auth.auth(login, password, app_id, 'offline, messages')[0]
		print(self.access_token)
		self.layer = ''
		self.uid = ''
		self.section = ''

	def dialog(self, uid=False):
		if uid != self.uid and uid:
			self.uid = uid
		self.layer = ""
		self.section = "dialog"
		dialog = json.loads(urllib2.urlopen("https://api.vk.com/method/messages.getHistory?count=20&user_id=%s&access_token=%s&v=5.33" % (self.uid, self.access_token)).read().decode("utf-8"))
		for item in reversed(dialog["response"]["items"]):
			user = json.loads(urllib2.urlopen("https://api.vk.com/method/users.get?user_id=%s&fields=contacts&access_token%s&v=5.8" % (item["from_id"],self.access_token)).read().decode("utf-8"))["response"][0];
			self.layer+= "%s %s (%s):\n" % (user["first_name"], user["last_name"], item["user_id"])
			self.layer+= "%s \n" % item["body"]
			self.layer+= "-------------------------------------------- \n"

	def dialogs(self):
		self.layer = ''
		self.section = 'dialogs'
		dialogs = json.loads(urllib2.urlopen("https://api.vk.com/method/messages.getDialogs?count=10&access_token=%s&v=5.33" % (self.access_token)).read().decode("utf-8"))
		for item in reversed(dialogs["response"]["items"]):
			user = json.loads(urllib2.urlopen("https://api.vk.com/method/users.get?user_id=%s&fields=contacts,online&access_token%s&v=5.8" % (item["message"]["user_id"],self.access_token)).read().decode("utf-8"))["response"][0];
			if (user["online"] == 1):
				user["online"] = "online"
			else:
				user["online"] = "offline"
			self.layer+= "%s %s [%s] (%s):\n" % (user["first_name"], user["last_name"], user["online"], item["message"]["user_id"])
			self.layer+= "%s \n" % item["message"]["body"]
			self.layer+= "--------------------------------------------\n"


	def send(self, message):
		message = urllib2.quote(message).encode('utf-8')
		dialog = json.loads(urllib2.urlopen("https://api.vk.com/method/messages.send?user_id=%s&message=%s&access_token=%s&v=5.33" % (self.uid, message, self.access_token)).read().decode("utf-8"))
		self.control('r')


	def control(self, input):
		print('----LOADING----')
		if input == 'd':
			self.dialogs()
		elif input == 'exit':
			os.system('clear')
			sys.exit(0)
		elif input == '':
			self.layer = ''
		elif self.section = 'dialogs':
			if input = 'r':
				self.dialogs()
			else:
				self.dialogs(input)
		os.system('clear')
		print(self.layer)
		self.control('%s' % raw_input('Enter the command: \n'))



if __name__ == '__main__':
	os.system('clear')
	vk = Connect(app_id, login, password)
	vk.control('')