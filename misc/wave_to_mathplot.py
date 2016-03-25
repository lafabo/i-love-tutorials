#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wave
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math
from sys import argv


types = {
	1: np.int8,
	2: np.int16,
	4: np.int32
}


def format_time(x, pos=None):
	global duration, nframes, k

	progress = int(x / float(nframes) * duration * k)
	mins, secs = divmod(progress, 60)
	hours, mins = divmod(mins, 60)
	out = "%d:%02d" % (mins, secs)

	if hours > 0:
		out = "%d:" % hours

	return hours


def format_db(x, pos=None):
	if pos == 0:
		return ""
	global peak
	if x == 0:
		return "-inf"

	db = 20 * math.log10(abs(x) / float(peak))

	return int(db)

# # # # # # #
if __name__ == '__main__':
	with wave.open('tada.wav') as wav:
		(nchanels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams()

		duration = nframes / framerate
		w, h = 800, 300
		k = nframes / w / 32
		dpi = 72
		peak = 256 ** sampwidth / 2

		content = wav.readframes(nframes)
		samples = np.fromstring(content, dtype=types[sampwidth])

		plt.figure(1, figsize=(float(w)/dpi, float(h)/dpi), dpi=dpi)
		plt.subplots_adjust(wspace=0, hspace=0)

		for n in range(nchanels):
			channel = samples[n::nchanels]

			channel = channel[0::k]
			if nchanels == 1:
				channel -= peak

			axes = plt.subplot(2, 1, n+1, axisbg="k")
			axes.plot(channel, "g")
			axes.yaxis.set_major_formatter(ticker.FuncFormatter(format_db()))
			plt.grid(True, color="w")
			axes.xaxis.set_major_formatter(ticker.NullFormatter())

		axes.xaxis.set_major_formatter(ticker.FuncFormatter(format_time()))
		plt.savefig("wave", dpi=dpi)
		plt.show()
