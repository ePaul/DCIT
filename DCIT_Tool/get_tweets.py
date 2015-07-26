#!/usr/bin/env python

# get_tweets.py
# Authors: Jessica E. Grasso & C. Clayton Violand

from bs4 import BeautifulSoup
import sys
import os
import re

class Tweet():

	def __init__(self, tweet, thread_tick):
		self._original = tweet["text"]
		# original tweet text, not modified
		self.raw = tweet["text"].lower()
		# tweet text, modified as needed
		self.words = [ i.lower() for i in tweet["text"].split() ]
		# tweet text tokenized
		self.id = tweet["id"].lower()
		# tweet ID (number)
		self.convo_id = thread_tick
		# ??
		self.user = tweet["user"].lower()
		# user ID (number)
		self.depth = tweet["depth"]
		# depth in conversation
		self.has_dc = False
		# does the tweet contain discourse connectives?
		self.ats = [ i.lower() for i in tweet["text"].split() if i.startswith("@") ]
		# words preceded with @ (replies)
		self.hashes = [ i.lower() for i in tweet["text"].split() if i.startswith("#") ]
		# word preceded with # (hashtags)

def tweet_scrape(file_path_argument=0):

	if file_path_argument==0: # if no argument given
		file_path = raw_input("Enter the path of XML (tweets) file to get convo pairs: ")
	
		# For testing, so we don't have to type/paste each time
		if file_path == 'r': # 'r' for "relative" path
			file_path =  "../tweets-xml/toy.xml"
		if file_path == 'j':
			file_path = "/Volumes/TWITTER/DCIT/tweets-xml/toy.xml"
		elif file_path == 'c':
			file_path = "/home/clayton/bin/DCIT/tweets-xml/toy.xml"
		else:
			assert os.path.exists(file_path), "File not found: "+str(file_path)

	else: # path passed to function as argument
		file_path = file_path_argument
		assert os.path.exists(file_path), "File not found: "+str(file_path)	

	print "Using file: " + str(file_path)		

	soup = BeautifulSoup(open(file_path), "html")

	# Creates list of Tweet objects.
	tweets = []
	thread_tick = 0
	for t in soup.find_all('thread'):
			thread_tick += 1
			for i in t.find_all('tweet'):
				tweet = Tweet(i, thread_tick)
				tweets.append(tweet)

	return tweets
