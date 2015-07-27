#!/usr/bin/env python

# test.py
# Authors: C. Clayton Violand & Jessica E. Grasso

from get_dcons import dcon_scrape
from get_tweets import tweet_scrape
from get_convoPairs import convoPair_scrape
from get_matches import get_matches
from get_stats import get_stats

def main ():
	#filepath_dimlex_j = "/Volumes/TWITTER/DCIT/connectives-xml/dimlex.xml"
	#filepath_tweetdirectory_j = "/Volumes/TWITTER/DCIT/tweets-xml/"
	filepath_dimlex_c = "/home/clayton/bin/DCIT/connectives-xml/dimlex.xml"
	filepath_tweetdirectory_c = "/home/clayton/bin/DCIT/tweets-xml/"
	
	# Get list of Discourse Connective objects. (extract from dimlex.xml)	
	dcons = dcon_scrape(filepath_dimlex_c)

	# json-tweets-2013-04-01.xml

	for i in range(1, 31): # 1 to 30
		if i < 10:
			day = "json-tweets-2013-04-0" + str(i) + ".xml"
		else:
			day = "json-tweets-2013-04-" + str(i) + ".xml"

		# Get list of Tweet objects. (extract from file)

		daytweets = tweet_scrape(filepath_tweetdirectory_c + day)
		matches_tweets = get_matches(daytweets, dcons, info, True)
		
	# Get list of Conversations amongst Tweets.
	# convoPairs = convoPair_scrape(filepath_toytweets_j)

if __name__ == "__main__":
	main()
	
