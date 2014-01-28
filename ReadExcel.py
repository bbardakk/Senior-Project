import xlrd
from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen
from pymongo import Connection

client = Connection()
collection = client.journalList.lastVersion
collection2 = client.dergi.tubitak

count = collection2.find().count()
count += 1
#print count
count2 = 0

for j in range(1,count):
	
	id = str(j)
	
	dergi = collection2.find_one({"id" : id})
	issn = dergi["issn"]
	group = dergi["group"]
	jour = dergi["jour"]

	book = xlrd.open_workbook("impact-factory.xlsx")
	sheet = book.sheet_by_index(0)

	for i in range(1, sheet.nrows):
		issn2 = sheet.cell(i,2).value
		impact = sheet.cell(i,4).value
		if(issn == issn2):
			entry = {
				"id" : id,
				"issn" : str(issn),
				"impact" : str(impact),
				"jour" : str(jour),
				"group" : str(group)
			}
			collection.insert(entry)
			count2 = 1
			print str(j)
			break
			#print str(i) 
	if count2 == 0:
		impact = ""
		entry = {
			"id" : id,
			"issn" : str(issn),
			"impact" : impact,
			"jour" : str(jour),
			"group" : str(group)
		}
		collection.insert(entry)
		print str(j)
	count2 = 0
