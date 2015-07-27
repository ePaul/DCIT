#!/usr/bin/env python

# get_matches.py
# Authors: C. Clayton Violand & Jessica E. Grasso

from collections import Counter
from disambiguate import disambiguate
import get_info

def get_matches_new(tweets, dcons, info):
	discontins = [i for i in dcons if i.sep == "discont"]
	hit_count_discontins = 0 # number of discontinuous Discourse Connectives

	contins = [i for i in dcons if i.sep == "cont"]
	hit_count_contins = 0 # number of discontinuous Discourse Connectives
	
	tweet_count = 0		# number of Tweets seen so far
	tweet_hit_count = 0	# number of Tweets containing a Discourse Connective.
	tweet_trigger = False

	for t in tweets:
		tweet_count += 1
		tweet_trigger = False
		
		# DISCONTINUOUS CASES
		for i in discontins:
			if i.type_part_one == "phrasal" and i.type_part_two == "single":
				if (" " + i.part_one + " ") in t.raw and (" " + i.part_two + " ") in t.raw and t.raw.find(i.part_one) < t.raw.find(i.part_two):
					tweet_trigger = True
					hit_count_discontins += 1
					# Remove found cases.
					t.raw = t.raw.replace(i.part_one, '')
					t.raw = t.raw.replace(i.part_two, '')

			# Switch Scenario.
			elif i.type_part_one == "single" and i.type_part_two == "phrasal":
				if (" " + i.part_one + " ") in t.raw and (" " + i.part_two + " ") in t.raw and t.raw.find(i.part_one) < t.raw.find(i.part_two):
					tweet_trigger = True
					hit_count_discontins += 1
					# Remove found cases.
					t.raw = t.raw.replace(i.part_one, '')
					t.raw = t.raw.replace(i.part_two, '')

			elif i.type_part_one == "single" and i.type_part_two == "single":
				if (" " + i.part_one + " ") in t.raw and (" " + i.part_two + " ") in t.raw and t.raw.find(i.part_one) < t.raw.find(i.part_two):
					tweet_trigger = True
					hit_count_discontins += 1
					# Remove found cases.
					t.raw = t.raw.replace(i.part_one, '')
					t.raw = t.raw.replace(i.part_two, '')

		# CONTINUOUS CASES
		for j in contins:
			if j.type_part_one == "phrasal":
				if j.part_one in t.raw:
					tweet_trigger = True
					hit_count_contins += 1
					# Remove found cases.
					t.raw = t.raw.replace(j.part_one, '')
			if j.type_part_one == "single":
				if j.part_one in t.raw:
					tweet_trigger = True
					hit_count_contins += 1
					# Remove found cases.
					t.raw = t.raw.replace(j.part_one, '')

		if tweet_trigger == True:
			tweet_hit_count += 1
			t.has_dc = True
	
	hit_count = hit_count_contins + hit_count_discontins
	
	# update info object	
	info.dcs_found += hit_count
	info.tweets += tweet_count
	info.tweets_with_dcs += tweet_hit_count
	info.continuous += hit_count_contins
	info.discontinuous += hit_count_discontins
		
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

