#!/usr/bin/env python
#  -*- coding: utf-8 -*-

import sys, requests

############################################
# todo del apiid before commit
settings = {"APPID": "176e61e392014ba3b76b64d8988b850d",
			"city": 'Moscow', "units": "metric", "lang": "DE"}
############################################

# check zip code or city name or error

if len(sys.argv) == 2:
	settings['city'] = sys.argv[1]

if isinstance(settings['city'], str):
	url = 'http://api.openweathermap.org/data/2.5/weather?q='


requesturl = url + settings['city'] + '&units=' + settings['units'] \
			 + '&lang=' +settings['lang'] + '&APPID=' + settings['APPID']

def get_weather(requesturl):
	try:
		response = requests.get(requesturl)
		if response.status_code != 200:
			response = 'N/A'
			return response
		else:
			weather_data = response.json()
			return weather_data
	except requests.exceptions.RequestException as error:
		print error
		sys.exit(1)


if __name__ == '__main__':
	weather = get_weather(requesturl)
	print '%s\t\t%r (%r %r)' % (weather['name'], weather['main']['temp'], weather['main']['temp_min'],weather['main']['temp_max'])