import xlrd
from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen
from pymongo import Connection

client = Connection()
collection = client.dergi.excel


book = xlrd.open_workbook("impact-factory.xlsx")
sheet = book.sheet_by_index(0)

for i in range(1, sheet.nrows):
	issn = sheet.cell(i,2).value
	impact = sheet.cell(i,4).value
	entry = {
		"id" : str(i),
		"issn" : str(issn),
		"impact" : str(impact)
	}
	collection.insert(entry)
	#print str(i) 
