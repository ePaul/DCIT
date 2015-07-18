#!/usr/bin/python

# get_convos.py
# Authors: Jessica E. Grasso & C. Clayton Violand

from bs4 import BeautifulSoup
import sys
import os

def convo_scrape():

	file_path = raw_input("Enter the path of XML (tweets) file to get convos: ")

	# For testing, so we don't have to type/paste each time
	if file_path == 'j':
		file_path = "/Volumes/TWITTER/DCIT/tweets-xml/toy.xml"
	elif file_path == 'c':
		file_path = "/home/clayton/bin/DCIT/tweets-xml/toy.xml"
	else:
		assert os.path.exists(file_path), "File not found: "+str(file_path)

	print "Using file: " + str(file_path)

	# get pairs
	soup = BeautifulSoup(open(file_path), "html")

	tweetlist = []
	for thread in soup.find_all('thread'):
		for tweet in thread.find_all('tweet'):
			tweetlist.append(tweet)

	convoPairsList = []

	for t in tweetlist:
		if t["depth"] != "0":
			newpair = t.parent["text"] + '\t' + t["text"]
			convoPairsList.append(newpair)

	# make new soup object and write pairs to xml file

	newsoup = BeautifulSoup(features='xml')

	for p in convoPairsList:
		newsoup.append(newsoup.new_tag("pair", text=p))
	
	# write to file (this will need to be changed)
	f = open('convoPairs.xml','w')
	f.write(newsoup.prettify().encode('utf8'))
	f.close()

	return convoPairsList
