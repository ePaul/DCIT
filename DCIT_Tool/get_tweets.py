#!/usr/bin/env python

# get_tweets.py
# Authors: Jessica E. Grasso & C. Clayton Violand

from bs4 import BeautifulSoup
import sys
import os
import re

class Tweet():

	def __init__(self, tweet, f):
		self.filename = f
	
		self._original = tweet["text"]
		# original tweet text, not modified
		self.raw = tweet["text"].lower()
		# tweet text, modified as needed
		self.words = [ i.lower() for i in tweet["text"].split() ]
		# tweet text tokenized
		self.id = tweet["id"].lower()
		# tweet ID (number)
		self.user = tweet["user"].lower()
		# user ID (number)
		self.depth = tweet["depth"]
		# depth in conversation
		
		self.has_dc = False
		# does the tweet contain discourse connectives?
		
		self.has_ambi_dc = False
		# does the tweet contain at least one ambiguous DC?  i.e. should we disambiguate?
		self.ambi_count_discontins = 0
		self.ambi_count_contins = 0
		# how many ambiguous DCs are in the tweet

		# is this enough, or do we need to remember where these are?

		self.ats = [ i.lower() for i in tweet["text"].split() if i.startswith("@") ]
		# words preceded with @ (replies)
		self.hashes = [ i.lower() for i in tweet["text"].split() if i.startswith("#") ]
		# word preceded with # (hashtags)

		
def tweet_scrape(file_path_argument=0):
# file_path_argument should be a single string or a list of strings

	 # if no argument given, prompt for file path
	if file_path_argument==0:
		file_path = raw_input("Enter the path of XML (tweets) file to get convo pairs: ")
	
		# For testing, so we don't have to type/paste each time
		if file_path == 'r': # 'r' for "relative" path
			file_path_list = [ "../tweets-xml/toy.xml" ]
		if file_path == 'j':
			file_path_list = ["/Volumes/TWITTER/DCIT/tweets-xml/toy.xml"]
		elif file_path == 'c':
			file_path_list = ["/home/clayton/bin/DCIT/tweets-xml/toy.xml"]
		else:
			file_path_list = [file_path]

	# list passed to function as argument, just rename	
	elif isinstance(file_path_argument, list):
		file_path_list = file_path_argument
	
	# if argument was string (or anything else), make it into list
	else: 
		file_path_list = [file_path_argument]
		
	# check if all files in list exist
	for f in file_path_list:
		assert os.path.exists(f), "File not found: "+str(f)
	print "Using files: " + str(file_path_list)


	for f in file_path_list:
		soup = BeautifulSoup(open(f), "html")
	
		# returns instance of tweet object
		for t in soup.find_all('thread'):
			for i in t.find_all('tweet'):
				tweet = Tweet(i,f)
				yield tweet # next element of the iterator

