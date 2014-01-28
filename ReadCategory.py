# -*- coding: utf-8 -*- 
from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

from pymongo import Connection

client = Connection()
db = client.journalList
collection = db.category

url = "http://www.thomsonscientific.com/cgi-bin/jrnlst/jlsubcatg.cgi?PC=D"
page = urlopen(url).read()

count = 0

for line in page.split('\n'):
	if line[:7] == '<OPTION':
		count += 1
		cat,catName = line.split('> ')
		#print str(cat[15:-2]) + " " + str(catName[:-10])
		entry = {
			"id" : str(count),
			"catName" : str(catName[:-10]),
			"cat" : str(cat[15:-2])
		}
		collection.insert(entry)
		#print str(cat) + " " + str(catName)

#print "Count:" + str(count)
