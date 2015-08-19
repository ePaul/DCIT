##!/usr/bin/env python
## -*- coding: utf-8 -*-
##
## test.py
## Authors: C. Violand & J. Grasso
##
 
def post_disambiguation_stats(tweets, dcons, info):
	# split the list of dcons, should only happen once
	discontins = [i for i in dcons if i.sep == "discont"]
	contins = [i for i in dcons if i.sep == "cont"]
	
	# for each tweet, get the stats
	for t in tweets:
	
		info.tweets += 1
				
		if t.has_dc():
			info.tweets_with_dcs += 1
			
		for d in t.dcs:
		
			if d[0] in dcons:
			# because Schneider 0s were removed
						
				if d[0].sep == "cont":
					info.continuous += 1
					if d[1] == True:	 # if ambiguous
						info.continuous_ambi += 1
				elif d[0].sep == "discont":
					info.discontinuous +=1
					if d[1] == True:	 # if ambiguous
						info.discontinuous_ambi += 1
						
		yield t