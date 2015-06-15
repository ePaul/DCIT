#!/usr/bin/env python

# test.py
# Authors: C. Clayton Violand & Jessica E. Grasso

from get_dcons import dcon_scrape
from get_tweets import tweet_scrape
#from get_convos import convo_scrape
from get_matches import get_matches
from get_stats_singles import get_stats_singles
from get_stats_phrasals import get_stats_phrasals

def main():
	# Get list of Tweet objects.
	tweets = tweet_scrape()

	# Get list of Conversations amongst Tweets.
#	convos = convo_scrape(tweets)

	# Get list of Discourse Connective objects.
	dcons = dcon_scrape()

	# Get list of matches (tuples) between Discoure Connectives and Tweets.
	matches = get_matches(tweets, dcons, True)

	# Get statistics, info about connectives.
#	get_stats(dcons, matches_singles, "a")
#	get_stats(dcons, matches_singles, "s")
#	get_stats(dcons, matches_singles, "p")

if __name__ == "__main__":
	main()
