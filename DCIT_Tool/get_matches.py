#!/usr/bin/env python

# get_matches.py
# Authors: C. Clayton Violand & Jessica E. Grasso

from collections import Counter
from disambiguate import disambiguate
import get_info

def get_matches(tweets, contins, discontins, info):
	
	tweet_trigger = False

	# info object now updated as we go
	for t in tweets:	# this is an iterator

		info.tweets += 1	# number of Tweets seen so far
		tweet_trigger = False

		# DISCONTINUOUS CASES
		for i in discontins:
			for j in range(len(i.ortho_blocks)):
				if i.type_part_one[j] == "phrasal" and i.type_part_two[j] == "single":
					if (" " + i.part_one[j] + " ") in t.raw and (" " + i.part_two[j] + " ") in t.raw and t.raw.find(i.part_one[j]) < t.raw.find(i.part_two[j]):						
						tweet_trigger = True
						t.dcs.append(i)
						info.discontinuous += 1		# number of discontinuous DCs
						# Remove found cases.
						t.raw = t.raw.replace(i.part_one[j], '')
						t.raw = t.raw.replace(i.part_two[j], '')
						#
						info.discontinuous_dict[i] += 1
						# Check for potential ambiguity, update Tweet object
						a = (i.ambi=='1')						
						if a":
							t.has_ambi_dc = True
							t.ambi_count_discontins += 1
							info.ambiguous_dict[i] += 1
						t.dcs.append(i,a)
				# Switch Scenario.
				elif i.type_part_one[j] == "single" and i.type_part_two[j] == "phrasal":
					if (" " + i.part_one[j] + " ") in t.raw and (" " + i.part_two[j] + " ") in t.raw and t.raw.find(i.part_one[j]) < t.raw.find(i.part_two[j]):
						tweet_trigger = True
						t.dcs.append(i)
						info.discontinuous += 1		# number of discontinuous DCs
						# Remove found cases.
						t.raw = t.raw.replace(i.part_one[j], '')
						t.raw = t.raw.replace(i.part_two[j], '')
						#
						info.discontinuous_dict[i] += 1
						# Check for potential ambiguity, update Tweet object
						a = (i.ambi=='1')						
						if a:
							t.has_ambi_dc = True
							t.ambi_count_discontins += 1
							info.ambiguous_dict[i] += 1
						t.dcs.append(i,a)

				elif i.type_part_one[j] == "single" and i.type_part_two[j] == "single":
					if (" " + i.part_one[j] + " ") in t.raw and (" " + i.part_two[j] + " ") in t.raw and t.raw.find(i.part_one[j]) < t.raw.find(i.part_two[j]):
						tweet_trigger = True
						info.discontinuous += 1		# number of discontinuous DCs
						# Remove found cases.
						t.raw = t.raw.replace(i.part_one[j], '')
						t.raw = t.raw.replace(i.part_two[j], '')
						#
						info.discontinuous_dict[i] += 1
						# Check for potential ambiguity, update Tweet object
						a = (i.ambi=='1')						
						if a:
							t.has_ambi_dc = True
							t.ambi_count_discontins += 1	
							info.ambiguous_dict[i] += 1
						t.dcs.append(i,a)
		# CONTINUOUS CASES
		for i in contins:
			for j in range(len(i.ortho_blocks)):
				if i.type_part_one[j] == "phrasal":
					if (" " + i.part_one[j] + " ") in t.raw:
						tweet_trigger = True
						t.dcs.append(i)
						info.continuous += 1	# number of continuous DCs
						# Remove found cases.
						t.raw = t.raw.replace(i.part_one[j], '')
						#
						info.continuous_dict[i] += 1					
						# Check for potential ambiguity, update Tweet object
						a = (i.ambi=='1')
						if a:
							t.has_ambi_dc = True
							t.ambi_count_contins += 1
							info.ambiguous_dict[i] += 1
						t.dcs.append(i,a)
				if i.type_part_one[j] == "single":
					if (" " + i.part_one[j] + " ") in t.raw:
						tweet_trigger = True
						t.dcs.append(i)
						info.continuous += 1	# number of continuous DCs
						# Remove found cases.
						t.raw = t.raw.replace(i.part_one[j], '')
						#
						info.continuous_dict[i] += 1					
						# Check for potential ambiguity, update Tweet object
						a = (i.ambi=='1')
						if a:
							t.has_ambi_dc = True
							t.ambi_count_contins += 1
							info.ambiguous_dict[i] += 1					
						t.dcs.append(i,a)

		if tweet_trigger == True:
			info.tweets_with_dcs += 1	# was called tweet_hit_count
								# number of Tweets containing at least one Discourse Connective.
			t.has_dc = True
	
		info.discontinuous_ambi += t.ambi_count_discontins
		info.continuous_ambi += t.ambi_count_contins
	
		# this is another iterator
		yield t

