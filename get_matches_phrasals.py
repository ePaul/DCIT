#!/usr/bin/env python

# get_matches_phrasals.py
# Authors: C. Clayton Violand & Jessica E. Grasso

def get_matches_phrasals(tweets, dcons):
	matches_phrasals = []
	word_hit_count = 0	# number of discourse connectives
	tweet_hit_count = 0
	tweet_trigger = False
	for t in tweets:
		if tweet_trigger == True:
			tweet_hit_count += 1
			t.has_dc = True
		tweet_trigger = False
		for d in dcons:
			if d.type == "phrasal":
				if d.name in t.raw:
					tweet_trigger = True
					word_hit_count += 1
					matches.append((t,d))

	ratio = tweet_hit_count / float(len(tweets))

	print
	print "--SUMMARY--"
	print "-----------------------------------"
	print "Pre-disambiguation"
	print "-----------------------------------"
	print "Discourse Connective Type: \"phrasal\""
	print "--------------------------------------------------------------------"
	print "Found %d Discourse Connectives amongst %d Tweets." % (word_hit_count, len(tweets))
	print "Found a Discourse Connective in %d out of %d Tweets." % (tweet_hit_count, len(tweets))
	print "Tweet Saturation is %f." % ratio
	print "--------------------------------------------------------------------"

	return matches_phrasals
