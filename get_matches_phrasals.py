#!/usr/bin/env python

# get_matches_phrasals.py
# Authors: C. Clayton Violand & Jessica E. Grasso

def get_matches_phrasals():
	matches_phrasals = []
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
					matches_phrasals.append((t,d))

	ratio = tweet_hit_count / float(len(tweets))

	print
	print "--SUMMARY--" 
	print "-----------------------------------"
	print "Discourse Connective Type: \"phrasal\""
	print "--------------------------------------------------------------------"
	print "Found %d Discourse Connectives amongst %d Tweets." % (word_hit_count, len(tweets))
	print "Found a Discourse Connective in %d out of %d Tweets." % (tweet_hit_count, len(tweets))
	print "Tweet Saturation is %f." % ratio
	print "--------------------------------------------------------------------"
	print

	return matches_phrasals
