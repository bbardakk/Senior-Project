# -*- coding: utf-8 -*- 
from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen
from pymongo import Connection

client = Connection()
db = client.journalList
collection = db.journal

for i in range(1,9):
	url = "http://science.thomsonreuters.com/cgi-bin/jrnlst/jlresults.cgi?PC=K&mode=print&Page=" + str(i)
	page = urlopen(url).read()

	for line in page.split('\n'):
		if line[:12] == '<DT><strong>':
			id,jour = line[12:-14].split(". ");
			jour[:1]
			entry = {
				"id" : id,
				"jour" : jour
			}
			collection.update({"id":id}, entry, upsert=True)
			#print id + " Oldu " + jour
