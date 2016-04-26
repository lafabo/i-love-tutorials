#!/usr/bin/env python
# -*- coding: utf-8 -*-
import SpeechRecognition as sr
import subprocess
import os


def wav_to_text(wav):
	r = sr.Recognizer()
	with sr.AudioFile(AUDIO_FILE) as source:
		audio = r.record(source) # read the entire audio file

	try:
	# for testing purposes, we're just using the default API key
	# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
	# instead of `r.recognize_google(audio)`
		return r.recognize_google(audio)

def mpegs_in_dir(path):
	exten = '.mp4'
	result = []
	for dirpath, dirnames, filenames in os.walk(path):
		for name in filenames:
			if name.lower().endswith(exten):
				result.append(os.path.join(dirpath, name))
	# return list
	return result

def convert_mpeg_to_mp3(mpeg_file):
	# filepath, filename = os.path.split(mpeg_file)
	command = 'ffmpeg -i %s -ab 160K -ac 2 -ar 44100 -vn %s' % (
		mpeg_file, mpeg_file + '.wav')
	subprocess.call(command)
	return mpeg_file + '.wav'


if __name__ == '__main__':
	pass