#!/usr/bin/env python

# get_matches.py
# Authors: C. Clayton Violand & Jessica E. Grasso

def get_matches(tweets, dcons, verbose = False):
	phrasals = [i for i in dcons if i.type == "phrasal"]
	matches_phrasals = []
	hit_count_phrasals = 0	# number of phrasal Discourse Connectives

	singles = [i for i in dcons if i.type == "single"]
	matches_singles = []
	hit_count_singles = 0	# number of single Discourse Connectives

	tweet_hit_count = 0		# number of Tweets containing a Discourse Connective.
	tweet_trigger = False

	for t in tweets:
		if tweet_trigger == True:
			tweet_hit_count += 1
			t.has_dc = True
		tweet_trigger = False
		for p in phrasals:
			if p.name in t.raw:
				tweet_trigger = True
				hit_count_phrasals += 1
				matches_phrasals.append((t,p))
				t.words = t.raw.replace(p.name, ' ').split()
		for s in singles:
			if s.name in t.words:
				tweet_trigger = True
				hit_count_singles += 1
				matches_singles.append((t,s))
	
	matches = matches_singles + matches_phrasals
	hit_count = hit_count_singles + hit_count_phrasals
	ratio = tweet_hit_count / float(len(tweets))

	if verbose:
		print
		print "--SUMMARY--"
		print "-----------------------------------"
		print "Pre-disambiguation"
		print "--------------------------------------------------------------------"
		print "Found %d Discourse Connectives amongst %d Tweets." % (hit_count, len(tweets))
		print "Found a Discourse Connective in %d out of %d Tweets." % (tweet_hit_count, len(tweets))
		print "Tweet Saturation is %f." % ratio
		print "--------------------------------------------------------------------"
		print "Discourse Connectives of type = 'single': %d " % len(matches_singles)
		print "Discourse Connectives of type = 'phrasal: %d" % len(matches_phrasals)
		print "--------------------------------------------------------------------"
		print

	return matches
