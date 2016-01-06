#!/usr/bin/env python
#  -*- coding: utf-8 -*-
'''
Python simple timer

Input seconds and get notification
'''

import time, sys, subprocess
# from wave import open as waveOpen
# from ossaudiodev import  open as ossOpen

def playsound():
	subprocess.check_output(['bash', '-c', 'aplay tada.wav'])


def userinput_to_seconds(userinput):
	seconds = 0
	for i, v in enumerate(userinput.split(":")[::-1]):
		seconds += int(v) * 60**i
	return seconds


def seconds_to_hms(seconds):
	units = {0: "seconds", 1: "minutes", 2: "hours"}
	out = []
	for i, v in enumerate(str(seconds).split(":")[::-1]):
		out.append("%s %s" % (int(v), units[i]))
	return out[::-1]


def timer():
	'The main function of the program'

	if len(sys.argv) > 1:                 #First arg - script name. If there was second arguments - it will use it. Else input
		userinput = sys.argv[1]
	else:
		userinput = raw_input('Enter(works only seconds): ') #('Enter the time H:M:S: ')

	progress = userinput_to_seconds(userinput)
	progressbar(progress)
	print "\n\nTime out!\a\a"
	playsound()


def progressbar(total):
	bar_len = 60


	for i in range(1, total+1):
		time.sleep(1)

		bar_x = int(round(i * bar_len / total)) # filled bar (percent)
		time_lasts_percent = int(round(i * 100 / total))
		bar = '=' * bar_x + '-' * (bar_len - bar_x)
		sys.stdout.write("\r[%s]%d%% time remain %r" % (bar, time_lasts_percent, (seconds_to_hms(total - i))))
		sys.stdout.flush()

		# print "\r[%s]%d%%" % (bar, time_lasts_percent) # todo - try to guess how make all of it without sys



timer()