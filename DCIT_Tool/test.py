#!/usr/bin/env python

# test.py
# Authors: C. Clayton Violand & Jessica E. Grasso

from get_dcons import dcon_scrape
from get_tweets import tweet_scrape
from get_convos import convo_scrape
from get_matches import get_matches
from get_stats import get_stats

def main ():
	# Get list of Discourse Connective objects.
	dcons = dcon_scrape()

	# Get list of Tweet objects.
	tweets = tweet_scrape()

	# Get list of Conversations amongst Tweets.
#	convos = convo_scrape()
	
	# Get list of matches (tuples) between Discoure Connectives and Tweets.
	matches = get_matches(tweets, dcons, True)

	# Get some statistics / info about the connectives
	# Add funcitonality to display ambiguous tweets and their surroudnding contexts (ambiguous analysis).
	# how many are schneider1s. How many are schneider2s. how many schneider1s can be resolved.
	# trigrams of ambiguous.
	# sentenc position of ambiguous.
	# IN SUMMATION: pull out features that we can use to disambiguate.
#	get_stats(dcons, matches, 10, 'a')

if __name__ == "__main__":
	main()
