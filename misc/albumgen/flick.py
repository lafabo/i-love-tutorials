'''
This download random images from flickr
'''

import urllib, re, random


url = "https://www.flickr.com/explore/interesting/7days"
regex = '<img src="([^"]+)".*>'

photolist = urllib.urlopen(url)
raw_data = photolist.read()
pattern = re.compile(regex)
download = re.findall(pattern, raw_data)

# first in download array is some yahoo statistics shit so we skip it
x = random.randint(1, len(download))
photo = download[x].replace('_m.', '_z.', 1)
#photo = photo.replace('farm2.staticflickr.com/', 'c2.staticflickr.com/2')
urllib.urlretrieve(photo, "local-filename.jpg")
