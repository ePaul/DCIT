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

	discontins = [i for i in dcons if i.sep == "discont"]
	contins = [i for i in dcons if i.sep == "cont"]

	schneiders = [('denn',1,['KON']),
					('doch',1,['KON']),
					('entgegen',1,['APPO','APPR']),
					('seit',1,['KOUS']),
					('seitdem',1,['KOUS']),
					('trotz',1,['APPR']),
					('während',1,['KOUS']),
					('wegen',1,['APPO','APPR']),
						('also',2,['ADV']),
						('auch',2,['ADV']),
						('außer',2,['APPR']),
						('da',2,['ADV','KOUS']),
						('darum',2,['ADV']),
						('nebenher',2,['ADV']),
						('nur',2,['ADV']),
						('so',2,['ADV']),
						('sonst',2,['ADV']),
						('soweit',2,['ADV','KOUS']),
						('zugleich',2,['ADV']),
					('und',0,79),
					('als',0,17),
					('auch',0,1),
					('wie',0,12),
					('so',0,37),
					('nur',0,1),
					('aber',0,145),
					('dann',0,144),
					('doch',0,80),
					('da',0,90),
					('denn',0,116),
					('also',0,58),
					('seit',0,21),
					('während',0,102),
					('darauf',0,13),
					('dabie',0,19),
					('allein',0,17),
					('wegen',0,191),
					('dafür',0,22),
					('daher',0,184),
					('sonst',0,56),
					('statt',0,37),
					('zugleich',0,81),
					('allerdings',0,167),
					('dagegen',0,148),
					('ferner',0,182),
					('trotz',0,180),
					('darum',0,80),
					('außer',0,15),
					('soweit',0,169),
					('entgegen',0,58),
					('danach',0,115),
					('wonach',0,14),
					('worauf',0,97),
					('weshalb',0,76),
					('seitdem',0,61),
					('womit',0,91),
					('aufgrund',0,0),
					('allenfalls',0,23),
					('wogegen',0,146),
					('nebenher',0,107),
					('weswegen',0,89)
				]			
																																						
	#contexts_for_schneider_twos	
	#contexts =	
	
	days = []
	# get all files in filepath_tweetdirectory (only those for which we also have tagged)
	# days = glob.glob(filepath_tweetdirectory+"*.xml")
	# Does not need to be sorted if filenames are correct.

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

	tweets = tweet_scrape(days)
	matched_tweets = get_matches(tweets, contins, discontins, tweetinfo_predisambiguation)
	
	disambiguated_tweets = disambiguate(matched_tweets, schneiders)
#	matched_disambiguated_tweets = get_matches(disambiguated_tweets, contins, discontins, tweetinfo_postdisambiguation)
	
	write_results(disambiguated_tweets, filepath_tweetdirectory, filepath_output)
	
	# Not Needed Now Because Write Does It.
	# this is needed because due to the iterator, disambiguated_tweets is generated on demand
	#for t in disambiguated_tweets:
	#	continue
		
	print "\n\n"
	print "-- PRE-DISAMBIGUATION"
	tweetinfo_predisambiguation.summary()

	print "\n\n"
	print "-- POST-DISAMBIGUATION"
	tweetinfo_postdisambiguation.summary()

if __name__ == "__main__":
	main()

