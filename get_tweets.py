#!/usr/bin/env python

# get_tweets.py
# Authors: Jessica E. Grasso & C. Clayton Violand

from bs4 import BeautifulSoup
import sys
import os

class Tweet():

	def __init__(self, tweet, thread_tick):
		self.id = tweet["id"].lower()
		self.convo_id = thread_tick
		self.user = tweet["user"].lower()
		self.depth = tweet["depth"]
		self.raw = tweet["text"].lower()
		self.words = [ i.lower() for i in tweet["text"].split() ]
		self.has_dc = False
		self.ats = [ i.lower() for i in tweet["text"].split() if i.startswith("@") ]
		self.hashes = [ i.lower() for i in tweet["text"].split() if i.startswith("#") ]

#	def __str__(self):
#		print tweet.id
#		print tweet.user
#		print tweet.depth
#		print tweet.raw
#		print tweet.words
#		print tweet.ats
#		print tweet.hashes

def tweet_scrape():
	file_path = raw_input("Enter path of XML (tweets) file: ")

	#################
	# For testing, so we don't have to type/paste each time
	if file_path == 'j':
		file_path = "/Volumes/TWITTER/DCIT/tweets-xml/toy.xml"
	elif file_path == 'c':
		file_path = "/Users/clayton/DCIT/tweets-xml/toy.xml"
	else:
		assert os.path.exists(file_path), "File not found: "+str(file_path)
	print "Using file: " + str(file_path)
	#################

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
