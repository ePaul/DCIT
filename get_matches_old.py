#!/usr/bin/env python

# get_matches.py
# Authors: C. Clayton Violand & Jessica E. Grasso

from collections import Counter
from disambiguate import disambiguate

def get_matches(tweets, dcons, verbose = False, write_xml = False):
	separables = [i for i in dcons if i.sep == "discont"]
	matches_separables = []
	hit_count_separables = 0 # number of discontinuous Discourse Connectives

	phrasals = [i for i in dcons if i.type == "phrasal" and i.sep == "cont"]
	matches_phrasals = []
	hit_count_phrasals = 0	# number of phrasal Discourse Connectives

	singles = [i for i in dcons if i.type == "single" and i.sep == "cont"]
	matches_singles = []
	hit_count_singles = 0	# number of single Discourse Connectives

	tweet_hit_count = 0		# number of Tweets containing a Discourse Connective.
	tweet_trigger = False

	for t in tweets:
		tweet_trigger = False
		for k in separables:
			if (" " + k.part_one + " ") in t.raw and (" " + k.part_two + " ") in t.raw and t.raw.find(k.part_one) < t.raw.find(k.part_two):
				tweet_trigger = True
				hit_count_separables += 1
				matches_separables.append((t,k))

				# Remove Separables before looking for Continuous (Phrasals and Singles).
				########
				t.raw = t.raw.replace(k.part_one, '')
				t.raw = t.raw.replace(k.part_two, '')
				########

		for p in phrasals:
			if p.part_one in t.raw:
				tweet_trigger = True
				hit_count_phrasals += 1
				matches_phrasals.append((t,p))

				# Remove Phrasals before looking for Singles.
				########
				t.raw = t.raw.replace(p.part_one, '')
				########

		for s in singles:
			if s.part_one in t.raw:
				tweet_trigger = True
				hit_count_singles += 1
				matches_singles.append((t,s))

		if tweet_trigger == True:
			tweet_hit_count += 1
			t.has_dc = True
	
	matches = matches_singles + matches_phrasals + matches_separables
	hit_count = hit_count_singles + hit_count_phrasals + hit_count_separables
	ratio = tweet_hit_count / float(len(tweets))

	ambiguous_cases = []
	ambiguous_singles = []
	ambiguous_phrasals = []
	ambiguous_separables = []
	for (t,s) in matches:
		if s.ambi == "1":
			ambiguous_cases.append(s)
	for (t,s) in matches_singles:
		if s.ambi == "1":
			ambiguous_singles.append(s.part_one)
	for (t,s) in matches_phrasals:
		if s.ambi == "1":
			ambiguous_phrasals.append(s.part_one)
	for (t,s) in matches_separables:
		if s.ambi == "1":
			ambiguous_separables.append(s.part_one + '*' + s.part_two)

	facts_singles = Counter(ambiguous_singles)
	facts_phrasals = Counter(ambiguous_phrasals)
	facts_separables = Counter(ambiguous_separables)

# testing disambiguation

	if verbose:
		print
		print "--SUMMARY--"
		print "NOTE: analysis done over one day of tweets (toy.xml)."
		print "--------------------------------------------------------------------"
		print		
		print "I. Pre-disambiguation: all matches."
		print "--------------------------------------------------------------------"
		print "Found %d potential Discourse Connective matches amongst %d Tweets." % (hit_count, len(tweets))
		print "Found a potential Discourse Connective in %d out of %d Tweets." % (tweet_hit_count, len(tweets))
		print "Potential Discourse Connective Saturation is %f." % ratio
		print "--------------------------------------------------------------------"
		print "of type = 'continuous single': %d " % len(matches_singles)
		print "of type = 'continuous phrasal: %d" % len(matches_phrasals)
		print "of type = 'discontinuous': %d " % len(matches_separables)
		print "--------------------------------------------------------------------"
		print		
		print "II. Pre-disambiguation: ambiguous matches."
		print "--------------------------------------------------------------------"
		print "Found %d ambiguous cases amongst %d matches." % (len(ambiguous_cases), hit_count)
		print "--------------------------------------------------------------------"
		print "of type = 'continuous single': %d " % len(ambiguous_singles)
		print "of type = 'continuous phrasal: %d" % len(ambiguous_phrasals)
		print "of type = 'discontinuous': %d " % len(ambiguous_separables)
		print "--------------------------------------------------------------------"
		print
		print "III. Ambiguity facts."
		print "--------------------------------------------------------------------"
		print "**Counts for ambiguous singles**"
		for i in facts_singles.most_common():
			print i, facts_singles[i]	
		print
		print "**Counts for ambiguous phrasals**"
		for i in facts_phrasals.most_common():
			print i, facts_phrasals[i]	
		print
		print "**Counts for ambiguous separables**"
		for i in facts_separables.most_common():
			print i, facts_separables[i]	
	return matches
