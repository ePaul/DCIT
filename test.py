#!/usr/bin/env python

# test.py
# Authors: C. Clayton Violand & Jessica E. Grasso

from get_dcons import dcon_scrape
from get_tweets import tweet_scrape
from get_matches_singles import get_matches_singles
from get_matches_phrasals import get_matches_phrasals
from get_stats_singles import get_stats_singles
from get_stats_phrasals import get_stats_phrasals


def main():
	# Get list of Tweet objects.
	tweets = tweet_scrape()

	# Get list of Conversations amongst Tweets.
#	convos = convo_compile(tweets)

	# Get list of Discourse Connective objects.
	dcons = dcon_scrape()

	# Check for occurances of Discourse Connectives (type=="single") in Tweets.
	matches_singles, num_dc = get_matches_singles(tweets, dcons)

	# Check for occurances of Discourse Connectives (type=="phrasal") in Tweets.
	matches_phrasals = get_matches_phrasals(tweets, dcons)

	# Get some statistics / info about the connectives
	get_stats_singles(dcons, matches_singles)
	get_stats_phrasals(dcons, matches_phrasals)

if __name__ == "__main__":
	main()
