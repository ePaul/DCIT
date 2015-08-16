#!/usr/bin/env python
# -*- coding: utf-8 -*-

# test.py
# Authors: C. Clayton Violand & Jessica E. Grasso

import os
import glob

from get_dcons import dcon_scrape
from get_tweets import tweet_scrape
from get_convoPairs import convoPair_scrape
from get_matches import get_matches
from get_info import Info
from disambiguate import disambiguate
from write_results import write_results

def main ():
	filepath_dimlex = "../connectives-xml/dimlex.xml"
	filepath_tweetdirectory = "../tweets-xml/"	
	filepath_output = "../results/"

	if not os.path.exists(filepath_output):
    		os.makedirs(filepath_output)

	# Get list of Discourse Connective objects (extract from dimlex.xml).
	dcons = dcon_scrape(filepath_dimlex)
	
	days = []
	# Get all files in filepath_tweetdirectory (only those for which we also have tagged).
	days = glob.glob(filepath_tweetdirectory+"*.xml")
	days = days[0:1]
	# TESTING.
	#days = filepath_tweetdirectory+"toy.xml"

	"""
	# using all the days we have
	for i in range(1, 31): # 1 to 30
		if i == 20:
			continue
		elif i < 10:
			day = "json-tweets-2013-04-0" + str(i) + ".xml"
		else:
			day = "json-tweets-2013-04-" + str(i) + ".xml"
		days.append(day)
	"""

	tweetinfo_predisambiguation = Info(dcons)
	tweetinfo_postdisambiguation = Info(dcons)

	tweets = tweet_scrape(days)
	matched_tweets = get_matches(tweets, dcons, tweetinfo_predisambiguation)
	
	disambiguated_tweets = disambiguate(matched_tweets, dcons)
#	matched_disambiguated_tweets = get_matches(disambiguated_tweets, contins, discontins, tweetinfo_postdisambiguation)
	
	write_results(disambiguated_tweets, filepath_tweetdirectory, filepath_output)
	
	# Not Needed Now Because Write Does It.
	# this is needed because due to the iterator, disambiguated_tweets is generated on demand
	#for t in disambiguated_tweets:
	#	continue
	"""	
	print "\n\n"
	print "-- PRE-DISAMBIGUATION"
	tweetinfo_predisambiguation.summary()

	print "\n\n"
	print "-- POST-DISAMBIGUATION"
	tweetinfo_postdisambiguation.summary()
	"""
if __name__ == "__main__":
	main()

