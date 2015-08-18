##!/usr/bin/env python
## -*- coding: utf-8 -*-
##
## test.py
## Authors: C. Violand & J. Grasso
##
 
def post_disambiguation_stats(tweets, dcons, info):

	for t in tweets:
		info.tweets += 1
		
		if t.has_dc:
			info.tweets_with_dcs += 1
			tweet_trigger = True
		
		for d in t.dcs:
			if d in dcons:
			# because Schneider 0s were removed
				if d[1] == True:
					if d[0].sep == "cont":
					elif d[0].sep == "discont":

		
		
	return info

