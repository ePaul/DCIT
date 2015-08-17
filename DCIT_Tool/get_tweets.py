##!/usr/bin/env python
##
## get_tweets.py
## Authors: J. Grasso & C. Violand
##

import os
import sys
import re

from bs4 import BeautifulSoup

class Tweet():
	'''
	Instance are Tweet objects instantiated by tweet_scrape(). Information 
	source is an .xml file. Methods defined are print_dcs(), which neatly prints 
	DiscourseConnectives matched within the Tweet object text.
	'''


	def __init__(self, tweet, f):
		self.filename = f
	
		# UNMODIFIED Tweet text.
		self._original = tweet["text"]
		# Modifed-as-need Tweet text.
		self.raw = tweet["text"].lower()
		# Tokenized Tweet text.
		self.words = [ i.lower() for i in tweet["text"].split() ]
		# Tweet ID.
		self.id = tweet["id"].lower()
		# Twitter user ID.
		self.user = tweet["user"].lower()
		# Conversation depth.
		self.depth = tweet["depth"]
		
		# Does the Tweet object contain (a) discourse connective(s)?
		self.has_dc = False		
		self.dcs = []
		
		# Does the Tweet object contain (an) ambiguous DC(s)?
		self.has_ambi_dc = False
		# How many of each type?
		self.ambi_count_discontins = 0
		self.ambi_count_contins = 0

		# Extras.
		self.ats = [ i.lower() for i in tweet["text"].split() if i.startswith("@") ]
		self.hashes = [ i.lower() for i in tweet["text"].split() if i.startswith("#") ]
	
	# Method for printing DiscourseConnective matches found in Tweet object.
	def print_dcs(self):
		print self._original + '\t'
		for d in self.dcs:
			print d[0].part_one[0], d[0].part_two[0],
		print
		
def tweet_scrape(file_path_argument=0): # Argument as string or list of strings.
	# Filepath handling.
	if file_path_argument==0:
		file_path = raw_input("Enter the path of XML (tweets) file to get convo pairs: ")
		### COMMENT OUT AFTER TESTING ###
		if file_path == 'r': # 'r' for "relative" path
			file_path_list = ["../tweets-xml/toy.xml"]
		if file_path == 'j':
			file_path_list = ["/Volumes/TWITTER/DCIT/tweets-xml/toy.xml"]
		elif file_path == 'c':
			file_path_list = ["/home/clayton/bin/DCIT/tweets-xml/toy.xml"]
		else:
			file_path_list = [file_path]
		###
	elif isinstance(file_path_argument, list):
		file_path_list = file_path_argument
	else: 
		file_path_list = [file_path_argument]
	for f in file_path_list:
		assert os.path.exists(f), "File not found: "+str(f)
	print "Using files: " + str(file_path_list)

	# Create soup objects from Tweet .xml files (returns as iterator).
	for f in file_path_list:
		file = os.path.basename(f)
		soup = BeautifulSoup(open(f), "html")
	
		# Find/create Tweet objects from soup objects.
		for t in soup.find_all('thread'):
			for i in t.find_all('tweet'):
				tweet = Tweet(i,file)

				yield tweet

