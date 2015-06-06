#!/usr/bin/env python

# get_dcons.py
# Authors: C. Clayton Violand & Jessica E. Grasso

from bs4 import BeautifulSoup
import sys
import os

class DiscourseConnective():

	def __init__(self, entry):
		self.name = entry.find("part").text
		self.type = entry.part["type"]
		self.ambi = entry.find("conn_d").text
		self.relation = entry.find("relation").text

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
#		print

def dcon_scrape():

	file_path = raw_input("Enter the path of XML (connectives) file: ")

	assert os.path.exists(file_path), "File not found: "+str(file_path)
	f = open(file_path,'r+')
	print "Using file: " + str(file_path)

	soup = BeautifulSoup(open(file_path), "xml")

	# Creates a list of DiscourseConnective objects.
	dcons = []
	for i in soup.find_all('entry'):
		dcon = DiscourseConnective(i)
		dcons.append(dcon)

	f.close()	
	return dcons
	