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
from disambiguate import *
from write_results import write_results
from post_disambiguation_stats import post_disambiguation_stats

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
<<<<<<< HEAD
	###	
	#days = glob.glob(filepath_tweetdirectory+"*.xml")

=======
	###
	#days = glob.glob(filepath_tweetdirectory+"*.xml")
	
>>>>>>> 50727311e5a2818ce9ac3ee153919a91feca1e6f
	# Initialize Info objects.
	tweetinfo_predisambiguation = Info(dcons)

	# Get Tweet objects (returns as iterator).
	tweets = tweet_scrape(days)
	# Get pre-disambiguation matches (returns as iterator).
	matched_tweets = get_matches(tweets, dcons, tweetinfo_predisambiguation)
	
	# Disambiguate matches containing ambiguity.
	# Schneider 0s	
	new_dcons = disambiguate_remove_zeroes(dcons)
	
	# Schneider 1s and 2s
	disambiguated_tweets = disambiguate(matched_tweets, dcons)
	# Get post-disambiguation matches.
	
	tweetinfo_postdisambiguation = Info(new_dcons)
		
	disambiguated_tweets2 = post_disambiguation_stats(disambiguated_tweets, new_dcons, tweetinfo_postdisambiguation)
		
	# Write results to .xml file.
	write_results(disambiguated_tweets2, filepath_tweetdirectory, filepath_output)

	# Print statistics summaries.
	print "\n\n"
	print "Pre-disambiguation"
	tweetinfo_predisambiguation.summary()
		
	print "\n\n"
	print "Post-disambiguation"
	tweetinfo_postdisambiguation.summary()

if __name__ == "__main__":
	main()

