##!/usr/bin/env python
## -*- coding: utf-8 -*-
##
## test.py
## Authors: C. Violand & J. Grasso
##

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
	# Filepath handling.
	filepath_dimlex = "../connectives-xml/dimlex.xml"
	filepath_tweetdirectory = "../tweets-xml/"	
	filepath_output = "../results/"
	if not os.path.exists(filepath_output):
		os.makedirs(filepath_output)

	# Get list of DiscourseConnective objects.
	dcons = dcon_scrape(filepath_dimlex)
	
	# Get list of files in filepath_tweetdirectory.
	days = []	
	### COMMENT OUT AFTER TESTING ###
	days = filepath_tweetdirectory + "toy.xml"
	###
	"""	
	days = glob.glob(filepath_tweetdirectory+"*.xml")
	
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

	# Initialize Info objects.
	tweetinfo_predisambiguation = Info(dcons)
	tweetinfo_postdisambiguation = Info(dcons)

	# Get Tweet objects (returns as iterator).
	tweets = tweet_scrape(days)
	# Get pre-disambiguation matches (returns as iterator).
	matched_tweets = get_matches(tweets, dcons, tweetinfo_predisambiguation)
	
	# Disambiguate matches containing ambiguity.
	disambiguated_tweets = disambiguate(matched_tweets, dcons)
	# Get post-disambiguation matches.
#	matched_disambiguated_tweets = get_matches(disambiguated_tweets, contins, discontins, tweetinfo_postdisambiguation)
	
	# Write results to .xml file.
	write_results(disambiguated_tweets, filepath_tweetdirectory, filepath_output)
	
	# Not Needed Now Because Write Does It.
	# this is needed because due to the iterator, disambiguated_tweets is 
	# generated on demand
#	for t in disambiguated_tweets:
#		continue

	# Print Statistics Summaries.
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

