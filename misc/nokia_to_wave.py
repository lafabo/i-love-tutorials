#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wave
import math
import re
from struct import pack
from sys import  argv

notes = {
	"-" : 0 ,
	"C" : 261.626,
	"#C" : 277.183,
	"D" : 293.665,
	"#D" : 311.127,
	"E": 329.628,
	"#E" : 349.228,
	"F" : 349.228,
	"#F" : 369.994,
	"G" : 391.995,
	"#G" : 415.305,
	"A" : 440.000,
	"#A" : 466.164,
	"B" : 493.883,
	"#B" : 523.251
}

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
	return 32 / duration, tone, octave

def append_freq(vol, freq, time):
	for i in range(0, time/10*441):
		result = (32765 * vol * math.sin(6.28*freq*i/44100))
		frames.append(result)

def append_note(vol, time, note, octave):
	for i in range(0,int(time/10.0*441)):
		freq = notes[note] * octave
		result = (32765*vol*math.sin(6.28*freq*i/44100))
		frames.append(result)

	if abs(math.sin(6.28*freq*i/44100)) > 0.01:
		while abs(math.sin(6.28*freq*i/44100)) > 0.01:
			result = (32765*vol*math.sin(6.28*freq*i/44100))
			frames.append(result)
			i += 1

def append_notes(vol, list, bpm):
	for each in list:
		duration, tone, octave = parse_tone(each)
		try:
			append_note(vol, int(duration*1000*7.5bpm), tone, octave)
		except:
			print 'error parsing %s' % each

		append_note(0, int(250*7.5/bpm), '-', 1)

def write_wave(name):
	with wave.open(name, 'w') as fl:
		fl.setparams((1, 2, 44100, 0, 'NONE', 'not compossed'))
		result = []
		for frame in frames:
			result.append(pack('h', frame))
		for each in result:
			fl.writeframes(each)

# # # # # # # # # # # # # # # # # # # # # # #
if __name__ == '__main__':
	frames = []