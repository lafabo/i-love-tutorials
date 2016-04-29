#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import sys
import os
import re

def get_img(url):
	html = str(urllib2.urlopen(url).read())
	imgsrc = re.match(html, '<img (.*?) id="pImage_0" (.*?) src="(.*?)"')
	imgsrc = imgsrc[2]
	








if __name__ == '__main__':
	url = sys.argv[1]

