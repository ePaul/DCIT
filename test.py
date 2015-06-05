#!/usr/bin/env python

# Authors: C. Clayton Violand & Jessica E. Grasso

from get_dcons import dcon_scrape
from get_tweets import tweet_scrape

def main():
	# Enter custom html and xml file_paths as function arguments below:
	tweets = tweet_scrape()
	dcons = dcon_scrape()

	# Check for occurances of discourse connectives (type=="single") in tweets.
	matches = []
	word_hit_count = 0
	tweet_hit_count = 0
	tweet_trigger = False
	for t in tweets:
		if tweet_trigger == True:
			tweet_hit_count += 1
		tweet_trigger = False
		for d in dcons:
			if d.type == "single":
				if d.name in t.words:
					tweet_trigger = True
					word_hit_count += 1
					matches.append((t,d))

	ratio = tweet_hit_count / float(len(tweets))

	print
	print "--SUMMARY--" 
	print "-----------------------------------"
	print "Discourse Connective Type: \"single\""
	print "--------------------------------------------------------------------"
	print "Found %d Discourse Connectives amongst %d Tweets." % (word_hit_count, len(tweets))
	print "Found a Discourse Connective in %d out of %d Tweets." % (tweet_hit_count, len(tweets))
	print "Tweet Saturation is %f." % ratio
	print "--------------------------------------------------------------------"
	print

if __name__ == "__main__":
	main()
