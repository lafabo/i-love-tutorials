#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wave
import math
import re
from struct import pack
from sys import  argv


def parse_tone(note):
	note = note.upper()
	if note.find('-') == -1:
		try:
			duration, octave = re.findall(r'[0-9]+', note)
		except:
			pass
	else:
		duration = re.findall(r'[0-9]+', note)[0]
		octave = 1
	tone = re.findall(r'[A-Z,#,-]+', note)[0]
	duration, octave = int(duration), int(octave)

	if note.find('.') != -1:
		duration /= 1.5
	return (32 / duration, tone, octave)


def append_freq(vol, freq, time):
	for i in range(0, time/10*441):
		result = (32765 * vol * math.sin(6.28*freq*i/44100))
		frames.append(result)


def append_note(vol, time, note, octave):



if __name__ == '__main__':
	frames = []