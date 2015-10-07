#!/usr/bin/env python

# get_dcons.py
# Authors: C. Clayton Violand & Jessica E. Grasso

from bs4 import BeautifulSoup
import sys
import os

class DiscourseConnective():

	def __init__(self, entry):
		self.type = entry.part["type"].lower()	
		# single or phrasal ()
		# !! This is not a feature of the DC but of each of its parts !!
		
		self.sep = entry.orth["type"].lower()	
		# cont(inuous) or discont(inuous)
		self.ambi = entry.find("conn_d").text.lower()
		# 1 = ambiguous; 2 = not ambiguous
		self.relation = entry.find("relation").text.lower()
		# type of connective relation (sequence, elaboration, etc.), often empty

		# TODO: Expand to include all orthographies from dimlex file (right now only standard (first) ortho entry.
		# IDEA : self.part_one and self.part_two will be lists of strings, not strings.
		
		self.part_one = entry.find("part").text.lower()

		if self.sep == 'discont':
			self.part_two = entry.find("orth").findAll("part")[1].text.lower()
		else:
			self.part_two = None

		# what are these two blocks doing?
		try:
			self.position = [ i.text.lower() for i in entry.findChildren("integr") ]
		except:
			self.position = None

		try:
			self.ordering = [ i.text.lower() for i in entry.findChildren("ordering") ]
		except:
			self.ordering = None

def dcon_scrape(file_path_argument=0):
	
	if file_path_argument==0: # if no argument given
		file_path = raw_input("Enter path of XML (connectives) file: ")
	
		# For testing, so we don't have to type/paste each time
		if file_path == 'r':
			file_path = "../connectives-xml/dimlex.xml"
		if file_path == 'j':
			file_path = "/Volumes/TWITTER/DCIT/connectives-xml/dimlex.xml"
		elif file_path == 'c':
			file_path = "/home/clayton/bin/DCIT/connectives-xml/dimlex.xml"

	else: # path passed to function as argument
		file_path = file_path_argument
		
	assert os.path.exists(file_path), "File not found: "+str(file_path)	

	print "Using file: " + str(file_path)	
	
	soup = BeautifulSoup(open(file_path), "xml")

	# Creates list of DiscourseConnective objects.
	dcons = []
	for i in soup.find_all('entry'):
		dcon = DiscourseConnective(i)
		dcons.append(dcon)
		
	return set(dcons)

