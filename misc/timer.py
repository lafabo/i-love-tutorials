#!/usr/bin/python
'''
Python simple timer

Input seconds and get notification
'''

import time
from wave import open as waveOpen
from ossaudiodev import  open as ossOpen

def playsound():
	'''trying to play wav file
	with only python standart lib
	and linux sound system'''
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


def timer():
	'''atually there is a timer'''
	timer = int(input('Enter the seconds: '))
	time.sleep(timer)

	print "Time out!"
	playsound()

timer()

# todo argpasre
# todo make sound works
# todo parse XX:XX:XX as H:M:S or if XX:XX -> M:S and etc