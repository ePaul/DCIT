#!/usr/bin/env python

# get_matches.py
# Authors: C. Clayton Violand & Jessica E. Grasso

from collections import Counter
from disambiguate import disambiguate
import get_info

def get_matches_new(tweets, dcons, info):
	separables = [i for i in dcons if i.sep == "discont"]
	hit_count_separables = 0 # number of discontinuous Discourse Connectives

	phrasals = [i for i in dcons if i.type == "phrasal" and i.sep == "cont"]
	hit_count_phrasals = 0	# number of phrasal Discourse Connectives

	singles = [i for i in dcons if i.type == "single" and i.sep == "cont"]
	hit_count_singles = 0	# number of single Discourse Connectives
	
	tweet_count = 0		# number of Tweets seen so far
	tweet_hit_count = 0	# number of Tweets containing a Discourse Connective.
	tweet_trigger = False

	for t in tweets:
		tweet_count += 1
		tweet_trigger = False
		for k in separables:
			if (" " + k.part_one + " ") in t.raw and (" " + k.part_two + " ") in t.raw and t.raw.find(k.part_one) < t.raw.find(k.part_two):
				tweet_trigger = True
				hit_count_separables += 1
				#matches_separables.append((t,k))

				# Remove Separables before looking for Continuous (Phrasals and Singles).
				########
				t.raw = t.raw.replace(k.part_one, '')
				t.raw = t.raw.replace(k.part_two, '')
				########

		for p in phrasals:
			if p.part_one in t.raw:
				tweet_trigger = True
				hit_count_phrasals += 1
				#matches_phrasals.append((t,p))

				# Remove Phrasals before looking for Singles.
				########
				t.raw = t.raw.replace(p.part_one, '')
				########

		for s in singles:
			if s.part_one in t.raw:
				tweet_trigger = True
				hit_count_singles += 1
				#matches_singles.append((t,s))

		if tweet_trigger == True:
			tweet_hit_count += 1
			t.has_dc = True
	
	hit_count = hit_count_singles + hit_count_phrasals + hit_count_separables
	
	# update info object	
	info.dcs_found += hit_count
	info.tweets += tweet_count
	info.tweets_with_dcs += tweet_hit_count
	info.single_continuous += hit_count_singles
	info.phrasal_continuous += hit_count_phrasals
	info.discontinuous += hit_count_separables
		
	# still missing - store information about most common DCs without lists
	# perhaps dictionary/ies in the info object that tracks DC and occurance?
	
	# also still missing - stats about which are ambiguous
	
	'''
	# these lists are probably going to cause problems!

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
	'''


