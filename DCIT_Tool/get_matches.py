#!/usr/bin/env python

# get_matches.py
# Authors: C. Clayton Violand & Jessica E. Grasso

from collections import Counter
from disambiguate import disambiguate
import get_info

def get_matches(tweets, dcons, info):
	discontins = [i for i in dcons if i.sep == "discont"]
	hit_count_discontins = 0 # number of discontinuous Discourse Connectives

	contins = [i for i in dcons if i.sep == "cont"]
	hit_count_contins = 0 # number of continuous Discourse Connectives
	
	tweet_count = 0		# number of Tweets seen so far
	tweet_hit_count = 0	# number of Tweets containing at least one Discourse Connective.
	tweet_trigger = False
	total_ambi_discontins = 0
	total_ambi_contins = 0

	for t in tweets:	# this is an iterator
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
					#
					info.discontinuous_dict[i] += 1
					# Check for potential ambiguity, update Tweet object
					if i.ambi == "1":
						t.has_ambi_dc = True
						t.ambi_count_discontins += 1
						info.ambiguous_dict[i] += 1
						# do we need to save more info here?

			# Switch Scenario.
			elif i.type_part_one == "single" and i.type_part_two == "phrasal":
				if (" " + i.part_one + " ") in t.raw and (" " + i.part_two + " ") in t.raw and t.raw.find(i.part_one) < t.raw.find(i.part_two):
					tweet_trigger = True
					hit_count_discontins += 1
					# Remove found cases.
					t.raw = t.raw.replace(i.part_one, '')
					t.raw = t.raw.replace(i.part_two, '')
					#
					info.discontinuous_dict[i] += 1
					# Check for potential ambiguity, update Tweet object
					if i.ambi == "1":
						t.has_ambi_dc = True
						t.ambi_count_discontins += 1
						info.ambiguous_dict[i] += 1
						# do we need to save more info here?

			elif i.type_part_one == "single" and i.type_part_two == "single":
				if (" " + i.part_one + " ") in t.raw and (" " + i.part_two + " ") in t.raw and t.raw.find(i.part_one) < t.raw.find(i.part_two):
					tweet_trigger = True
					hit_count_discontins += 1
					# Remove found cases.
					t.raw = t.raw.replace(i.part_one, '')
					t.raw = t.raw.replace(i.part_two, '')
					#
					info.discontinuous_dict[i] += 1
					# Check for potential ambiguity, update Tweet object
					if i.ambi == "1":
						t.has_ambi_dc = True
						t.ambi_count_discontins += 1	
						info.ambiguous_dict[i] += 1
						# do we need to save more info here?
		# CONTINUOUS CASES
		for j in contins:
			if j.type_part_one == "phrasal":
				if j.part_one in t.raw:
					tweet_trigger = True
					hit_count_contins += 1
					# Remove found cases.
					t.raw = t.raw.replace(j.part_one, '')
					#
					info.continuous_dict[j] += 1					
					# Check for potential ambiguity, update Tweet object
					if j.ambi == "1":
						t.has_ambi_dc = True
						t.ambi_count_contins += 1
						info.ambiguous_dict[j] += 1
						# do we need to save more info here?
			if j.type_part_one == "single":
				if j.part_one in t.raw:
					tweet_trigger = True
					hit_count_contins += 1
					# Remove found cases.
					t.raw = t.raw.replace(j.part_one, '')
					#
					info.continuous_dict[j] += 1					
					# Check for potential ambiguity, update Tweet object
					if j.ambi == "1":
						t.has_ambi_dc = True
						t.ambi_count_contins += 1
						info.ambiguous_dict[j] += 1					
						# do we need to save more info here?

		if tweet_trigger == True:
			tweet_hit_count += 1
			t.has_dc = True
	
		total_ambi_discontins += t.ambi_count_discontins
		total_ambi_contins += t.ambi_count_contins
	
	hit_count = hit_count_contins + hit_count_discontins
	
	# update info object	
	info.dcs_found += hit_count
	info.tweets += tweet_count
	info.tweets_with_dcs += tweet_hit_count
	info.continuous += hit_count_contins
	info.discontinuous += hit_count_discontins
	
	info.continuous_ambi += total_ambi_contins
	info.discontinuous_ambi += total_ambi_discontins
	
		
	# still missing - store information about most common DCs without lists
	# perhaps dictionary/ies in the info object that tracks DC and occurance?
		
