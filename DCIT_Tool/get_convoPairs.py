#!/usr/bin/python

# get_convosPairs.py
# Authors: Jessica E. Grasso & C. Clayton Violand

from bs4 import BeautifulSoup
import sys
import os


class ConvoPair():

	def __init__(self, tweet1, tweet2):
	
		self._tweet1 = tweet1["text"]
		self._tweet2 = tweet2["text"]
		pairtext = tweet1["text"] + '\t' + tweet2["text"]
		self._original = pairtext
		# original tweet & pair text, not modified
		
		self.raw = pairtext.lower()
		# pair text, modified as needed
		
		self.words = [ i.lower() for i in pairtext.split() ]
		# pair text tokenized
		
		self.id1 = tweet1["id"].lower()
		self.id2 = tweet2["id"].lower()
		# tweet ID (number)

		self.user1 = tweet1["user"].lower()
		self.user2 = tweet2["user"].lower()
		# user ID (number)

		self.depth1 = tweet1["depth"]
		self.depth2 = tweet2["depth"]
		# depth in conversation
		
		self.has_dc = False
		# does the pair contain discourse connectives?
		
		self.ats = [ i.lower() for i in pairtext.split() if i.startswith("@") ]
		# words preceded with @ (replies)
		self.hashes = [ i.lower() for i in pairtext.split() if i.startswith("#") ]
		# words preceded with # (hashtags)



def convoPair_scrape(file_path_argument=0):

	if file_path_argument==0: # if no argument given
		file_path = raw_input("Enter the path of XML (tweets) file to get convo pairs: ")
	
		# For testing, so we don't have to type/paste each time
		if file_path == 'r': # 'r' for "relative" path
			file_path_list = "../tweets-xml/toy.xml"
		if file_path == 'j':
			file_path = "/Volumes/TWITTER/DCIT/tweets-xml/toy.xml"
		elif file_path == 'c':
			file_path = "/home/clayton/bin/DCIT/tweets-xml/toy.xml"

	else: # path passed to function as argument
		file_path = file_path_argument

	assert os.path.exists(file_path), "File not found: "+str(file_path)	

	print "Using file: " + str(file_path)	


	# get pairs
	
	soup = BeautifulSoup(open(file_path), "html")

	tweetlist = []
	for thread in soup.find_all('thread'):
		for tweet in thread.find_all('tweet'):
			tweetlist.append(tweet)

	convoPairs = []

	for t in tweetlist:
		# ignore top-level tweets
		if t["depth"] != "0":
			# ignore replies to empty top-level tweets
			if t.parent["text"] != "":			
				newpair = ConvoPair(t.parent, t)
				convoPairs.append(newpair)

	return convoPairs
