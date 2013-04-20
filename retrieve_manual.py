import urllib2, sys
def retrieve(link, filename='RedAlien.png'):
	page=urllib2.urlopen(link)
	contents = page.read()
	start = contents.find('id="header-img')
	start = contents.find('src=', start)+5
	end = contents.find('"',start)
	piclink = contents[start:end]
	size = urllib2.urlopen(piclink).info().getheaders("Content-Length")
	print "Downloading image. Size: %s bytes." % size[0]
	output = open(filename, 'wb')
	output.write(urllib2.urlopen(piclink).read())
	output.close()
url=raw_input('Please insert the URL: ')
retrieve(url)