##!/usr/bin/env python
## -*- coding: utf-8 -*-
##
## get_matches.py
## Authors: C. Violand & J. Grasso
##

from collections import Counter

def get_matches(tweets, dcons, info):
	tweet_trigger = False
	discontins = [i for i in dcons if i.sep == "discont"]
	contins = [i for i in dcons if i.sep == "cont"]
	
	for t in tweets:
		info.tweets += 1	# number of Tweets seen so far
		tweet_trigger = False
	
		# DISCONTINUOUS CASES
		for i in discontins:
		
			for j in range(len(i.ortho_blocks)):
				if i.type_part_one[j] == "phrasal" and i.type_part_two[j] == "single":
					if (" " + i.part_one[j] + " ") in t.raw and (" " + i.part_two[j] + " ") in t.raw and t.raw.find(i.part_one[j]) < t.raw.find(i.part_two[j]):						
						tweet_trigger = True
						# Update count of discontinuous DCs.
						info.discontinuous += 1
						info.discontinuous_dict[i] += 1
						
						# Remove found cases.
						t.raw = t.raw.replace(i.part_one[j], '')
						t.raw = t.raw.replace(i.part_two[j], '')

						# Check for potential ambiguity and update Tweet object.
						a = (i.ambi=='1')						
						if a:
							t.has_ambi_dc = True
							t.ambi_count_discontins += 1
							info.ambiguous_dict[i] += 1
						b = t._original.lower().find(i.part_one[j])
						t.dcs.append((i,a,b))

				# Check for the alternate scenario (where type_part_one is 
				# single and type_part_two is phrasal.
				elif i.type_part_one[j] == "single" and i.type_part_two[j] == "phrasal":
					if (" " + i.part_one[j] + " ") in t.raw and (" " + i.part_two[j] + " ") in t.raw and t.raw.find(i.part_one[j]) < t.raw.find(i.part_two[j]):
						tweet_trigger = True
						# Update count of discontinuous DCs.
						info.discontinuous += 1
						info.discontinuous_dict[i] += 1
						
						# Remove found cases.
						t.raw = t.raw.replace(i.part_one[j], '')
						t.raw = t.raw.replace(i.part_two[j], '')

						# Check for potential ambiguity and update Tweet object.
						a = (i.ambi=='1')						
						if a:
							t.has_ambi_dc = True
							t.ambi_count_discontins += 1
							info.ambiguous_dict[i] += 1
						b = t._original.lower().find(i.part_one[j])
						t.dcs.append((i,a,b))

				# Check for the last alternate scenario.
				elif i.type_part_one[j] == "single" and i.type_part_two[j] == "single":
					if (" " + i.part_one[j] + " ") in t.raw and (" " + i.part_two[j] + " ") in t.raw and t.raw.find(i.part_one[j]) < t.raw.find(i.part_two[j]):
						tweet_trigger = True
						# Update count of discontinuous DCs.
						info.discontinuous += 1
						info.discontinuous_dict[i] += 1

						# Remove found cases.
						t.raw = t.raw.replace(i.part_one[j], '')
						t.raw = t.raw.replace(i.part_two[j], '')
						
						# Check for potential ambiguity and update Tweet object.
						a = (i.ambi=='1')						
						if a:
							t.has_ambi_dc = True
							t.ambi_count_discontins += 1	
							info.ambiguous_dict[i] += 1
						b = t._original.lower().find(i.part_one[j])
						t.dcs.append((i,a,b))

		# CONTINUOUS CASES
		for i in contins:
			for j in range(len(i.ortho_blocks)):
				if i.type_part_one[j] == "phrasal":
					if (" " + i.part_one[j] + " ") in t.raw:
						tweet_trigger = True
						# Update count of discontinuous DCs.
						info.continuous += 1
						info.continuous_dict[i] += 1

						# Remove found cases.
						t.raw = t.raw.replace(i.part_one[j], '')
					
						# Check for potential ambiguity and update Tweet object.
						a = (i.ambi=='1')
						if a:
							t.has_ambi_dc = True
							t.ambi_count_contins += 1
							info.ambiguous_dict[i] += 1
						b = t._original.lower().find(i.part_one[j])
						t.dcs.append((i,a,b))

				# Check for alternate Scenario.
				if i.type_part_one[j] == "single":
					if (" " + i.part_one[j] + " ") in t.raw:
						tweet_trigger = True
						# Update count of discontinuous DCs.
						info.continuous += 1
						info.continuous_dict[i] += 1	

						# Remove found cases.
						t.raw = t.raw.replace(i.part_one[j], '')
				
						# Check for potential ambiguity and update Tweet object.
						a = (i.ambi=='1')
						if a:
							t.has_ambi_dc = True
							t.ambi_count_contins += 1
							info.ambiguous_dict[i] += 1					
						b = t._original.lower().find(i.part_one[j])
						t.dcs.append((i,a,b))

		if tweet_trigger == True:
			info.tweets_with_dcs += 1
	
		info.discontinuous_ambi += t.ambi_count_discontins
		info.continuous_ambi += t.ambi_count_contins
	
		yield t

