#!/usr/bin/env python

# get_dcons.py
# Authors: C. Clayton Violand & Jessica E. Grasso

from bs4 import BeautifulSoup
import sys
import os

class DiscourseConnective():

	def __init__(self, entry):
		self.name = entry.find("part").text.lower()
		self.type = entry.part["type"].lower()
		self.ambi = entry.find("conn_d").text.lower()
		self.relation = entry.find("relation").text.lower()

		if entry.find("integr"):
			self.position = [ i for i in entry.find("integr").text ]
		else:
			self.position = None

		if entry.find("ordering"):
			self.ordering = [ i for i in entry.find("ordering").text ]
		else:
			self.ordering = None

#	def __str__(self):
#		print type(dcon.name)
#		print type(dcon.type)
#		print type(dcon.ambi)
#		print type(dcon.relation)
#		print type(dcon.position)
#		print type(dcon.ordering)

def dcon_scrape():
	file_path = raw_input("Enter the path of XML (connectives) file: ")

	# For testing, so we don't have to type/paste each time
	# of course, later we will automate this to use all 30 files, but for testing just 1
	if file_path == 'j':
		file_path = "/Volumes/TWITTER/DCIT/connectives-xml/dimlex.xml"
	#else if file_path == 'c':
	#	file_path = CLAY, add yours here to save some time when running it!
	else:
		assert os.path.exists(file_path), "File not found: "+str(file_path)	
	
	print "Using file: " + str(file_path)	
	
	soup = BeautifulSoup(open(file_path), "xml")

	# Creates a list of DiscourseConnective objects.
	dcons = []
	for i in soup.find_all('entry'):
		dcon = DiscourseConnective(i)
		dcons.append(dcon)
		
	return set(dcons)
	