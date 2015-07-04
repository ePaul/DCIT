#!/usr/bin/env python

# test.py
# Authors: C. Clayton Violand & Jessica E. Grasso

from get_dcons import dcon_scrape
from get_tweets import tweet_scrape
from get_stats import get_stats
#from get_convos import convo_scrape

from get_matches import get_matches


def main():
	# Get list of Tweet objects.
	tweets = tweet_scrape()

	# Get list of Conversations amongst Tweets.

	#convos = convo_scrape(tweets)

	# Get list of Discourse Connective objects.
	dcons = dcon_scrape()
	
	for d in dcons:
		print d.name

	# Get list of matches (tuples) between Discoure Connectives and Tweets.
	matches = get_matches(tweets, dcons, True)

	# Get some statistics / info about the connectives
	get_stats(dcons, matches_singles, 10, 'a')

if __name__ == "__main__":
	main()
