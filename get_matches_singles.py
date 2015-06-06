#!/usr/bin/env python

# get_matches_singles.py
# Authors: C. Clayton Violand & Jessica E. Grasso

def get_matches_singles(tweets, dcons):
	matches_singles = []
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
					matches_singles.append((t,d))
	
	ratio = tweet_hit_count / float(len(tweets))

	print
	print "--SUMMARY--"
	print "-----------------------------------"
	print "Pre-disambiguation"
	print "-----------------------------------"
	print "Discourse Connective Type: \"single\""
	print "--------------------------------------------------------------------"
	print "Found %d Discourse Connectives amongst %d Tweets." % (word_hit_count, len(tweets))
	print "Found a Discourse Connective in %d out of %d Tweets." % (tweet_hit_count, len(tweets))
	print "Tweet Saturation is %f." % ratio
	print "--------------------------------------------------------------------"

	return matches_singles
