# -*- coding: utf-8 -*- 
from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen
from pymongo import Connection

client = Connection()
db = client.journalList
collection = db.journal

collection2 = client.dergi.tubitak
group = ""

for i in range(1,3752):

	id = str(i)

	dergi = collection.find_one({"id":id})
	jour = dergi["jour"]
	issn = dergi["issn"]
	 
	url = "http://www.ulakbim.gov.tr/cabim/ubyt/dergiler.php?kw="+issn+"&journal_group=&index_type=&the_year=2012"
	page = urlopen(url).read()

	for line in page.split('\n'):
		if line[:9] == "<tr style":
			group = (line.split("<td")[5])[16:-5]
			#print group

	entry = {
		"id" : id,
		"issn" : str(issn),
		"jour" : str(jour),
		"group" : group
	}
	collection2.insert(entry)

	group = ""
