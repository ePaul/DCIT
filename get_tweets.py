#!/usr/bin/env python

# get_tweets.py
# Authors: Jessica E. Grasso & C. Clayton Violand

from bs4 import BeautifulSoup

#class Conversation(object):

#	def __init__(self):

class Tweet():

	def __init__(self, tweet):
		self.id = str(tweet["id"])
		self.user = str(tweet["user"])
		self.depth = int(tweet["depth"])
		self.raw = tweet["text"]
		self.words = tweet["text"].split()
		self.ats = [ i for i in tweet["text"].split() if i.startswith("@") ]
		self.hashes = [ i for i in tweet["text"].split() if i.startswith("#") ]

#	def __str__(self):
#		print tweet.id
#		print tweet.user
#		print tweet.depth
#		print tweet.raw
#		print tweet.ats
#		print tweet.hashes
#		print

def tweet_scrape(file_path = "/Users/clayton/DCIT/tweets-html/conversations-2013-04-01.html"):
	soup = BeautifulSoup(open(file_path), "html")

	# Creates a list of Tweet objects.
	tweets = []
	for i in soup.find_all('tweet'):
		tweet = Tweet(i)
		tweets.append(tweet)

	return tweets
