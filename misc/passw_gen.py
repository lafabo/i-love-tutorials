#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from random import choice

allowed_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz,./<>?;\':"[]{}\|!@#$%^&*()-=_+'


def gen_pwd(pwd_lenth):
	new_pwd = ''
	iterations = 0

	# 1 upper (any unicode), 1 lower, 1 number, one symbol, **N** chars minimum.
	# there is something not working yet
	while not re.match(r'/^((?=\S*?[A-Z])(?=\S*?[a-z])(?=\S*?[0-9]).{6,})\S$/', new_pwd):
		for i in range(int(pwd_lenth)):
			new_pwd += choice(allowed_chars)
		iterations += 1
	#else:
	return new_pwd, iterations

if __name__ == '__main__':
	pwd_len = int(input('Enter the len of your new password: '))
	res = gen_pwd(pwd_len)
	print('Your new password is: \n\n\n%s\n\ngenerated in %s iterations' % (res[0], res[1]))

