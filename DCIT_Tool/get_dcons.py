##!/usr/bin/env python
## -*- coding: utf-8 -*-
##
## get_dcons.py
## Authors: C. Violand & J. Grasso
##

import os
import sys

from bs4 import BeautifulSoup

class DiscourseConnective():
	'''
	Instances are DiscourseConnective objects instantiated by dcon_scrape().
	Information source is an .xml (dimlex) file.
	'''

	def __init__(self, entry):	
		# CONTINUITY.
		self.sep = entry.orth["type"].lower()
		self.ortho_blocks = entry.findAll("orth")	

		# PART ONE.
		self.type_part_one = [ i.find("part")["type"].lower() for i in self.ortho_blocks ]
		self.part_one = [ i.find("part").text.lower() for i in self.ortho_blocks ]

		# PART TWO.
		if self.sep == 'discont':
			self.type_part_two = [ i.findAll("part")[1]["type"].lower() for i in self.ortho_blocks ]
			self.part_two = [ i.findAll("part")[1].text.lower() for i in self.ortho_blocks ]
		else:
			self.type_part_two = [None]
			self.part_two = [None]
		
		# AMBIGUITY.
		self.ambi = entry.find("conn_d").text.lower()

		# EXTRAS.
		self.relation = entry.find("relation").text.lower()
		try:
			self.position = [ i.text.lower() for i in entry.findChildren("integr") ]
		except:
			self.position = None
		try:
			self.ordering = [ i.text.lower() for i in entry.findChildren("ordering") ]
		except:
			self.ordering = None


def dcon_scrape(file_path_argument=0):
	# Filepath handling.
	if file_path_argument==0:
		file_path = raw_input("Enter path of XML (connectives) file: ")
		### COMMENT OUT AFTER TESTING ###
		if file_path == 'r':
			file_path = "../connectives-xml/dimlex.xml"
		if file_path == 'j':
			file_path = "/Volumes/TWITTER/DCIT/connectives-xml/dimlex.xml"
		elif file_path == 'c':
			file_path = "/home/clayton/bin/DCIT/connectives-xml/dimlex.xml"
		###
	else:
		file_path = file_path_argument
	assert os.path.exists(file_path), "File not found: "+str(file_path)	
	print "Using dimlex file: " + str(file_path)	
	
	# Create soup object of dimlex file.
	soup = BeautifulSoup(open(file_path), "xml")

	# Create list of DiscourseConnective objects.
	dcons = []
	for i in soup.find_all('entry'):
		dcon = DiscourseConnective(i)
		dcons.append(dcon)

	return set(dcons)

