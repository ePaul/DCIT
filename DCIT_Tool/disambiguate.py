#!/usr/env/python coding
# -*- coding: utf-8 -*-

# Authors: C. Clayton Violand & Jessica E. Grasso

import re
import string

def disambiguate(tweets, schneiders):
	pattern = re.compile(r'[a-zA-ZäöüßÄÖÜẞ]+\/[a-zA-ZäöüßÄÖÜẞ]+\/[A-ZÄÖÜẞ]+')
	#tagged_tweet_id = re.compile('r') # TODO: PULL OUT 18 DIGIT ID.

	for t in tweets:
		# maybe better to pass relative path in as argument?
		tagged_path = "../tweets-POS_tagged/"+t.filename + "-tagged.txt"
		tagged = open(tagged_path)
		
		for line in tagged:
			# find line that matches (maybe too slow for big files? use grep?)
			if line.find(t.id) >= 0:
			
				# remains unchanged
				results = re.findall(pattern,line)
				instances = {}
				for i in results:
					parts = string.split(i,'/')
			
					if parts[1] in instances.keys():
						continue
					else:
						instances[parts[1]] = (parts[0], parts[2])
			
				for i in range(len(schneiders)):
					if schneiders[i][1] == 1:
						for j in instances:
							if schneiders[i][0] == j:
								if instances[j][1] in schneiders[i][2]:
									pass
									# match instance IDs to IDs in tweets file and add flag property.
					# Add functionality for context Schneiders. For now, just save to run stats.
					elif schneiders[i][1] == 2:
						pass
					# Add funcitonality for rest. For now, just save to run stats.
					else:
						pass
						
		yield t