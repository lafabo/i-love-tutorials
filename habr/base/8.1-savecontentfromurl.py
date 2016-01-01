import urllib2, os
from BeautifulSoup import BeautifulSoup

url_adr = str(raw_input('Enter the URL: '))
url = urllib2.urlopen(url_adr)
soup = BeautifulSoup(url)
# getting all content urls (images for example)

for image in soup.findAll('img'):
	name = '8-tmp/%s' % os.path.basename(image.get('src'))
	imgfile = open(name, 'w')
	#imgfile.write(image.get('src'))
	for line in (urllib2.urlopen(image.get('src'))).readlines():
		imgfile.write(line)


