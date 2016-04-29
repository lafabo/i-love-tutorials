#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pynder
import time

fb_id = ''
fb_auth_token = ''


def look_for_new_users():
	session = pynder.Session(fb_id, fb_auth_token)
	users = session.nearby_users()
	return users


def timer():
	while True:
		time.sleep(60)


notify = False


def notify(users):
	if users and len(users) > 0:
		return True
	return False


if __name__ == '__main__':
	pass

#todo Make this s*t work