##!/usr/bin/env python

# test.py
# Authors: C. Clayton Violand & Jessica E. Grasso

from get_dcons import dcon_scrape
from get_tweets import tweet_scrape
from get_convoPairs import convoPair_scrape
from get_matches import get_matches

from get_info import Info

def main ():
	filepath_dimlex = "../connectives-xml/dimlex.xml"
	filepath_tweetdirectory = "../tweets-xml/"
	filepath_toydirectory = "../tweets-xml/toy.xml"
	
	# Get list of Discourse Connective objects. (extract from dimlex.xml)	
	dcons = dcon_scrape(filepath_dimlex)

	days = []
	for i in range(1, 31): # 1 to 30
		if i == 20:
			continue
		elif i < 10:
			day = "json-tweets-2013-04-0" + str(i) + ".xml"
		else:
			day = "json-tweets-2013-04-" + str(i) + ".xml"
		days.append(day)

	tweetinfo = Info(dcons)

	# Get list of Tweet objects. (extract from file)
	tweets = tweet_scrape(filepath_toydirectory)
	matches = get_matches(tweets, dcons, tweetinfo, True)
		
	tweetinfo.summary()

if __name__ == "__main__":
	main()

