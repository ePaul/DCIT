#!/usr/bin/python

# get_convos.py
# Authors: Jessica E. Grasso & C. Clayton Violand

from bs4 import BeautifulSoup
import sys
import os

class Conversation():

	def __init__(self):
		self.complete = False
		self.depth = 1
		

def convo_scrape():
	file_path = raw_input("Enter the path of XML (tweets) file to get convos: ")

	# For testing, so we don't have to type/paste each time
	if file_path == 'j':
		file_path = "/Volumes/TWITTER/DCIT/tweets-xml/toy.xml"
	elif file_path == 'c':
		file_path = "/Users/clayton/DCIT/tweets-xml/toy.xml"
	else:
		assert os.path.exists(file_path), "File not found: "+str(file_path)

	print "Using file: " + str(file_path)

	soup = BeautifulSoup(open(file_path), "html")

	# Creates a list of Conversation objects.
	convos = []

	for thread in soup.find_all('thread'):
		tlist = []
		for tweet in thread.find_all('tweet'):
			tlist.append(tweet)
			
	print tlist
				


	return convos
