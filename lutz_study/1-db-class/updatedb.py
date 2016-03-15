#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shelve


with shelve.open('peoples') as db:
	sue = db['sue']
	sue.giveRaise(.25)
	db['sue'] = sue

	tom = db['tom']
	tom.giveRaise(.20)
	db['tom'] = tom
