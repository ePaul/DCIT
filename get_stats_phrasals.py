#!/usr/bin/python

# get_stats_phrasals.py
# Authors: C. Clayton Violand & Jessica E. Grasso

# !!! Did not test this yet, need get_matches_phrasals() function from Clay


def get_stats_phrasals(dcons, tuples):
	# tuples is a list of tuples (tweet, discourse_connector)
	dcons_dict = dict()
	for dc in dcons:
		if dc.type == "phrasal":
			dcons_dict[dc] = 0
	
	for t,d in tuples:
		# increment count in dictionary for each discourse connective
		dcons_dict[d] += 1
	
	# total number of dc's is the sum of all values in dictionary
	total = sum(dcons_dict.values())
	
	for key in sorted(dcons_dict, key=dcons_dict.get, reverse=True):
		print key.name, "occurs ", dcons_dict[key], " times, which is ", float(dcons_dict[key])/float(total)*100, " percent."
	
	return dcons_dict