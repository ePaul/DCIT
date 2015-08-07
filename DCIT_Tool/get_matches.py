#!/usr/bin/env python

# get_matches.py
# Authors: C. Clayton Violand & Jessica E. Grasso

from collections import Counter
from disambiguate import disambiguate
import get_info
import xml.etree.cElementTree as ET

#root = ET.Element("html")
#meta = ET.SubElement(root,"meta")
#body = ET.SubElement(meta,"body")

def get_matches(tweets, dcons, info, write = True):
	discontins = [i for i in dcons if i.sep == "discont"]
	hit_count_discontins = 0 # number of discontinuous Discourse Connectives

	contins = [i for i in dcons if i.sep == "cont"]
	hit_count_contins = 0 # number of continuous Discourse Connectives
	
	tweet_count = 0		# number of Tweets seen so far
	tweet_hit_count = 0	# number of Tweets containing at least one Discourse Connective.
	tweet_trigger = False
	total_ambi_discontins = 0
	total_ambi_contins = 0

	currentfile = ""
	for t in tweets:	# this is an iterator
		if t.filename != currentfile:
			if currentfile != "":			
				outfile = open(currentfile+"_new.xml")  
				outfile.write(soup.prettify())
				outfile.close()
			currentfile = t.filename
			soup = BeautifulSoup(open(currentfile), "html")
		t.id

		tweet_count += 1
		tweet_trigger = False
		
		# DISCONTINUOUS CASES
		for i in discontins:
			for j in range(len(i.ortho_blocks)):
				if i.type_part_one[j] == "phrasal" and i.type_part_two[j] == "single":
					if (" " + i.part_one[j] + " ") in t.raw and (" " + i.part_two[j] + " ") in t.raw and t.raw.find(i.part_one[j]) < t.raw.find(i.part_two[j]):
						tweet_trigger = True
						hit_count_discontins += 1
						# Remove found cases.
						t.raw = t.raw.replace(i.part_one[j], '')
						t.raw = t.raw.replace(i.part_two[j], '')
						#
						info.discontinuous_dict[i] += 1
						# Check for potential ambiguity, update Tweet object
						if i.ambi == "1":
							t.has_ambi_dc = True
							t.ambi_count_discontins += 1
							info.ambiguous_dict[i] += 1
							# do we need to save more info here?

				# Switch Scenario.
				elif i.type_part_one[j] == "single" and i.type_part_two[j] == "phrasal":
					if (" " + i.part_one[j] + " ") in t.raw and (" " + i.part_two[j] + " ") in t.raw and t.raw.find(i.part_one[j]) < t.raw.find(i.part_two[j]):
						tweet_trigger = True
						hit_count_discontins += 1
						# Remove found cases.
						t.raw = t.raw.replace(i.part_one[j], '')
						t.raw = t.raw.replace(i.part_two[j], '')
						#
						info.discontinuous_dict[i] += 1
						# Check for potential ambiguity, update Tweet object
						if i.ambi == "1":
							t.has_ambi_dc = True
							t.ambi_count_discontins += 1
							info.ambiguous_dict[i] += 1
							# do we need to save more info here?

				elif i.type_part_one[j] == "single" and i.type_part_two[j] == "single":
					if (" " + i.part_one[j] + " ") in t.raw and (" " + i.part_two[j] + " ") in t.raw and t.raw.find(i.part_one[j]) < t.raw.find(i.part_two[j]):
						tweet_trigger = True
						hit_count_discontins += 1
						# Remove found cases.
						t.raw = t.raw.replace(i.part_one[j], '')
						t.raw = t.raw.replace(i.part_two[j], '')
						#
						info.discontinuous_dict[i] += 1
						# Check for potential ambiguity, update Tweet object
						if i.ambi == "1":
							t.has_ambi_dc = True
							t.ambi_count_discontins += 1	
							info.ambiguous_dict[i] += 1
						# do we need to save more info here?

		# CONTINUOUS CASES
		for i in contins:
			for j in range(len(i.ortho_blocks)):
				if i.type_part_one[j] == "phrasal":
					if i.part_one[j] in t.raw:
						tweet_trigger = True
						hit_count_contins += 1
						# Remove found cases.
						t.raw = t.raw.replace(i.part_one[j], '')
						#
						info.continuous_dict[i] += 1					
						# Check for potential ambiguity, update Tweet object
						if i.ambi == "1":
							t.has_ambi_dc = True
							t.ambi_count_contins += 1
							info.ambiguous_dict[i] += 1
							# do we need to save more info here?
				if i.type_part_one[j] == "single":
					if i.part_one[j] in t.raw:
						tweet_trigger = True
						hit_count_contins += 1
						# Remove found cases.
						t.raw = t.raw.replace(i.part_one[j], '')
						#
						info.continuous_dict[i] += 1					
						# Check for potential ambiguity, update Tweet object
						if i.ambi == "1":
							t.has_ambi_dc = True
							t.ambi_count_contins += 1
							info.ambiguous_dict[i] += 1					
							# do we need to save more info here?

		if tweet_trigger == True:
			tweet_hit_count += 1
			t.has_dc = True
	
		total_ambi_discontins += t.ambi_count_discontins
		total_ambi_contins += t.ambi_count_contins

		test = ET.Element("test_%s" % t.id) 
		tree = ET.ElementTree(test)
		newline = "\n"
		tree.write("outfile")

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
		
