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

	# Get list of Discourse Connective objects. (extract from dimlex.xml)	
	dcons = dcon_scrape(filepath_dimlex)
	# lists of dcons by type
	discontins = [i for i in dcons if i.sep == "discont"]
	contins = [i for i in dcons if i.sep == "cont"]

	# Add type 0s and finish type 2s.
	# 1 = Connectives distinguishable by POS with 80% Precision (Schneider).
	# 2 = Connectives w/ ngrams POS w/ context.
	# 0 = The rest.
	schneiders = [('denn',1,['KON']),('doch',1,['KON']),('entgegen',1,['APPO','APPR']),('seit',1,['KOUS']),('seitdem',1,['KOUS']),('trotz',1,['APPR']),('während',1,['KOUS']),('wegen',1,['APPO','APPR']),('also',2,),('auch',2,),('außer',2,),('da',2,),('darum',2,),('nebenher',2,),('nur',2,),('so',2,),('sonst',2,),('soweit',2,)]

	days = []
	
	# get all files in filepath_tweetdirectory (only those for which we also have tagged)
	# days = glob.glob(filepath_tweetdirectory+"*.xml")
	# does this list need to be sorted?

	# for testing, only one day
	days = filepath_tweetdirectory+"toy.xml"

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


	# iterator over tweets, extract one at a time from .xml file(s)
	tweets = tweet_scrape(days)
	# iterator over tweets after they've gone through get_matches and been updated accordingly
	matched_tweets = get_matches(tweets, contins, discontins, tweetinfo_predisambiguation)
	
	disambiguated_tweets = disambiguate(matched_tweets, schneiders)
	# TODO: finish disambiguation 
	
	write_results(disambiguated_tweets, filepath_tweetdirectory, filepath_output)
	
	# this is needed because due to the iterator, disambiguated_tweets is generated on demand
	#for t in disambiguated_tweets:
	#	continue
		
	# TODO: get_matches-like function for after disambiguation, pass 
	# tweetinfo_postdisambiguation to this function to compare
		
	print "\n\n"
	print "-- PRE-DISAMBIGUATION"
	tweetinfo_predisambiguation.summary()

	print "\n\n"
	print "-- POST-DISAMBIGUATION"
	tweetinfo_postdisambiguation.summary()

if __name__ == "__main__":
	main()

