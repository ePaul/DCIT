##!/usr/env/python coding
## -*- coding: utf-8 -*-
##
## Authors: C. Violand & J. Grasso
##

## TODO: FINISH SCHNEIDER ONES; TWOS; PASS OUT ZEROS.

import re
import string

def disambiguate(tweets, dcons, zeros_limit = 0.8):
	# Schneiders -->
	# DiscourseConnective objects that qualify for a certain amount of 
	# disambiguation confidence based on 1 of 3 disambiguation methods as 
	# defined in "Bachelorarbeit_Angela_Schneider_735923".
	schneiders = [('denn',1,['KON']),
					('doch',1,['KON']),
					('entgegen',1,['APPO','APPR']),
					('seit',1,['KOUS']),
					('seitdem',1,['KOUS']),
					('trotz',1,['APPR']),
					('während',1,['KOUS']),
					('wegen',1,['APPO','APPR']),
						('also',2,['ADV']),
						('auch',2,['ADV']),
						('außer',2,['APPR']),
						('da',2,['ADV','KOUS']),
						('darum',2,['ADV']),
						('nebenher',2,['ADV']),
						('nur',2,['ADV']),
						('so',2,['ADV']),
						('sonst',2,['ADV']),
						('soweit',2,['ADV','KOUS']),
						('zugleich',2,['ADV']),
					('und',0,79),
					('als',0,17),
					('auch',0,1),
					('wie',0,12),
					('so',0,37),
					('nur',0,1),
					('aber',0,145),
					('dann',0,144),
					('doch',0,80),
					('da',0,90),
					('denn',0,116),
					('also',0,58),
					('seit',0,21),
					('während',0,102),
					('darauf',0,13),
					('dabie',0,19),
					('allein',0,17),
					('wegen',0,191),
					('dafür',0,22),
					('daher',0,184),
					('sonst',0,56),
					('statt',0,37),
					('zugleich',0,81),
					('allerdings',0,167),
					('dagegen',0,148),
					('ferner',0,182),
					('trotz',0,180),
					('darum',0,80),
					('außer',0,15),
					('soweit',0,169),
					('entgegen',0,58),
					('danach',0,115),
					('wonach',0,14),
					('worauf',0,97),
					('weshalb',0,76),
					('seitdem',0,61),
					('womit',0,91),
					('aufgrund',0,0),
					('allenfalls',0,23),
					('wogegen',0,146),
					('nebenher',0,107),
					('weswegen',0,89)
					]
																									
	# Contexts For Schneiders type '2'.		
	contexts = {
		'also' : [re.compile(r',\/,\/\$, [a-zA-ZäöüßÄÖÜẞ]+\/also\/ADV [a-zA-ZäöüßÄÖÜẞ]+\/[a-zA-ZäöüßÄÖÜẞ]+\/VFIN'), 
				  re.compile(r'.\/.\/\$. [a-zA-ZäöüßÄÖÜẞ]+\/also\/ADV [a-zA-ZäöüßÄÖÜẞ]+\/[a-zA-ZäöüßÄÖÜẞ]+\/VFIN'),
				  re.compile(r'[a-zA-ZäöüßÄÖÜẞ]+\/[a-zA-ZäöüßÄÖÜẞ]+\/VFIN [a-zA-ZäöüßÄÖÜẞ]+\/also\/ADV'),
				  re.compile(r'\?\/\?\/\$. [a-zA-ZäöüßÄÖÜẞ]+\/also\/ADV [a-zA-ZäöüßÄÖÜẞ]+\/[a-zA-ZäöüßÄÖÜẞ]+\/ADV')],
		'auch' : [],
		'außer': [],
		'da' : [],
		'darum' : [],
		'nebenher': [],
		'nur' : [],
		'so' : [],
		'sonst' : [],
		'soweit' : [],
		'zugleich' : []
		}

	# Create new mutable copy of dcons.
	new_dcons = dcons
	for d in new_dcons.copy():
		for s in schneiders:
			# HANDLING FOR SCHNEIDERS TYPE '0'.
			if s[1] == 0:
				if (d.part_one[0].encode("utf-8") == s[0]) and ((200-s[2]) / float(200)) >= zeros_limit :			
					# Remove this Schneider from new_dcons list as they qualify
					# as unambiguous.				
					new_dcons.remove(d)					

	# File handling for tweets-pos-tagged files.
	for t in tweets:
		tagged_path = "../tweets-pos-tagged/" + t.filename + "-tagged.txt"
		tagged = open(tagged_path)
		
		# Retrieve/create dictionary of information from tweets-pos-tagged 
		# files using a regular expression.
		pattern = re.compile(r'[a-zA-ZäöüßÄÖÜẞ]+\/[a-zA-ZäöüßÄÖÜẞ]+\/[A-ZÄÖÜẞ]+')
		for line in tagged:
			if line.find(t.id) >= 0:
				results = re.findall(pattern,line)
				instances = {}
				for i in results:
					parts = string.split(i,'/')
					if parts[1] in instances.keys():
						continue
					else:
						instances[parts[1]] = (parts[0], parts[2])

				to_delete = []
				# Iterate over DC matches associated with current Tweet object.
				for x in t.dcs:
					# If DC occurance is cited as ambiguous.
					if x[1] == True:
						# For each Schneider:
						for j in range(len(schneiders)):
							# If the Schneider matches the DC occurance.
							if x[0].part_one[0].encode("utf-8") == schneiders[j][0] and x[0].part_two == [None]:
								'''				
								# HANDLING FOR SCHNEIDERS TYPE '1'.
								if schneiders[j][1] == 1:									
									for k in instances:
										if schneiders[j][0] == k:
											if instances[k][1] in schneiders[j][2]:
												pass							
								'''

								# HANDLING FOR SCHNEIDERS TYPE '2'.
								if schneiders[j][1] == 2:
									context_found = False
									for k in contexts[schneiders[j][0]]:
										if re.search(k, line):
											context_found = True
									if not context_found:
										to_delete.append(x)

				### COMMENT OUT AFTER TESTING ###
				print len(t.dcs)
				###

				for item in to_delete:
					t.dcs.remove(item)	

				### COMMENT OUT AFTER TESTING ###		
				print len(t.dcs)
				print "-----"
				###

		yield t

