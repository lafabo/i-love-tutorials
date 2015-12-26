#!/usr/bin/python
'''
Python simple timer

Input seconds and get notification
'''

import time, sys, subprocess
# from wave import open as waveOpen
# from ossaudiodev import  open as ossOpen

def playsound():
	'''trying to play wav file
	with only python standart lib
	and linux sound system'''

	subprocess.check_output(['bash','-c', 'aplay tada.wav'])


	''' - don't work and i don't know why. Cannot find device /dev/dsp ._.

	wavfile = waveOpen('tada.wav', 'rb')
	(nc, sw, fr, nf, comptype, compname) = wavfile.getparams()
	dsp = ossOpen('/dev/dsp', 'w')

	try:
		from ossaudiodev import AFMT_S16_NE
	except ImportError:
		if byteorder == 'little':
			AFMT_S16_NE = ossaudiodev.AFMT_S16_LE
		else:
			AFMT_S16_NE = ossaudiodev.AFMT_S16_BE

	dsp.setparameters(AFMT_S16_NE, nc, fr)
	data = wavfile.readframes(nr)
	s.close()
	dsp.write(data)
	dsp.close()
	'''


def userinput_to_seconds(userinput):

	if str(userinput).count(':') == 0: #int(userinput):
		seconds = int(userinput)

	elif str(userinput).lstrip(':').isdigit():

		if str(userinput).count(':') == 1:
			print userinput + 'ONE!!!11'
			userinput = str(userinput).split(':')
			seconds = int(userinput[1]) + int(userinput[0]) * 60

		elif str(userinput).count(':') == 2:
			print userinput
			userinput = str(userinput).split(':')
			seconds = int(userinput[2]) + int(userinput[1]) * 60 + int(userinput[0]) * 3600

	else:
		# print "Write H:M:S or M:S or S"
		print 'Still works only seconds '
		timer()

	return seconds


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
		sys.stdout.write("\r[%s]%d%% time remain %d seconds" % (bar, time_lasts_percent, (total - i)))
		sys.stdout.flush()

		# print "\r[%s]%d%%" % (bar, time_lasts_percent) # todo - try to guess how make all of it without sys



timer()

# todo parse XX:XX:XX as H:M:S or if XX:XX -> M:S and etc
