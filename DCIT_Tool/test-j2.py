#!/usr/bin/env python

# test.py
# Authors: C. Clayton Violand & Jessica E. Grasso

from get_dcons import dcon_scrape
from get_tweets import tweet_scrape
from get_convoPairs import convoPair_scrape
from get_matches import get_matches
from get_stats import get_stats

def main ():
	filepath_dimlex_j = "../connectives-xml/dimlex.xml"

	# Get list of Discourse Connective objects. (extract from dimlex.xml)	
	dcons = dcon_scrape(filepath_dimlex_j)

	# Get list of Tweet objects. (extract from files)
	tweets = tweet_scrape(filepath_toytweets_j)
	
	# Get list of matches (tuples) between Discoure Connectives and Tweets.
	matches_tweets = get_matches(all_tweets, dcons, True)


	# Get list of Conversations amongst Tweets.
	convoPairs = convoPair_scrape(filepath_toytweets_j)
	
	# Matches should work with conversation pairs, too, since that class now has a self.raw
	matches_convoPairs = get_matches(all_convoPairs, dcons, True)

	# Get some statistics / info about the connectives
	# Add funcitonality to display ambiguous tweets and their surroudnding contexts (ambiguous analysis).
	# how many are schneider1s. How many are schneider2s. how many schneider1s can be resolved.
	# trigrams of ambiguous.
	# sentenc position of ambiguous.
	# IN SUMMATION: pull out features that we can use to disambiguate.
#	get_stats(dcons, matches, 10, 'a')

if __name__ == "__main__":
	main()
	
'''


for i in os.listdir(os.getcwd()):
    if i.endswith(".asm") or i.endswith(".py"): 
        ##print i
        continue
    else:
        continue

'''
