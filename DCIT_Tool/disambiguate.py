#!/usr/env/python coding
# -*- coding: utf-8 -*-

# Authors: C. Clayton Violand & Jessica E. Grasso

import re
import string

def disambiguate(tweets, schneiders, zeros_limit):
	pattern = re.compile(r'[a-zA-ZäöüßÄÖÜẞ]+\/[a-zA-ZäöüßÄÖÜẞ]+\/[A-ZÄÖÜẞ]+')

	for t in tweets:
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
	#			for i in range(len(schneiders)):
	#				if schneiders[i][1] == 0:
	#					if float(schneiders[i][2]) >= float(zeros_limit) * 200 or float(schneiders[i][2]) <= 200 - (200 * float(zeros_limit)):					
	#						pass					
					for schneiders[i][1] == 1:
						for j in instances:
							if schneiders[i][0] == j:
								if instances[j][1] in schneiders[i][2]:
									pass
					elif schnedier[i][2]:
						pass
						
		yield t
