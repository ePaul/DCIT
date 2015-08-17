##!/usr/env/python coding
## -*- coding: utf-8 -*-
##
## Authors: C. Violand & J. Grasso
##

## TODO: FINISH SCHNEIDER TWOS.

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
						('also',2),
						('auch',2),
						('außer',2),
						('da',2),
						('darum',2),
						('nebenher',2),
						('nur',2),
						('so',2),
						('sonst',2),
						('soweit',2),
						('zugleich',2),
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
				  re.compile(r'\.\/\.\/\$\. [a-zA-ZäöüßÄÖÜẞ]+\/also\/ADV [a-zA-ZäöüßÄÖÜẞ]+\/[a-zA-ZäöüßÄÖÜẞ]+\/VFIN'),
				  re.compile(r'[a-zA-ZäöüßÄÖÜẞ]+\/[a-zA-ZäöüßÄÖÜẞ]+\/VFIN [a-zA-ZäöüßÄÖÜẞ]+\/also\/ADV')],
		'auch' : [re.compile(r'[a-zA-ZäöüßÄÖÜẞ]+\/auch\/ADV [a-zA-ZäöüßÄÖÜẞ]+\/[a-zA-ZäöüßÄÖÜẞ]+\/VVFIN')],
		'außer': [],
		'da' : [re.compile(r',\/,\/\$, [a-zA-ZäöüßÄÖÜẞ]+\/da\/ADV'),
				re.compile(r'[a-zA-ZäöüßÄÖÜẞ]+\/da\/KOUS')],
		'darum' : [],
		'nebenher': [re.compile(r'\.\/\.\/\$\. [a-zA-ZäöüßÄÖÜẞ]+\/nebenher\/ADV [a-zA-ZäöüßÄÖÜẞ]+\/[a-zA-ZäöüßÄÖÜẞ]+\/VVFIN')],
		'nur' : [re.compile(r'\.\/\.\/\$\. [a-zA-ZäöüßÄÖÜẞ]+\/nur\/ADV [a-zA-ZäöüßÄÖÜẞ]+\/[a-zA-ZäöüßÄÖÜẞ]+\/VVFIN')],
		'so' : [re.compile(r',\/,\/\$, [a-zA-ZäöüßÄÖÜẞ]+\/so\/ADV [a-zA-ZäöüßÄÖÜẞ]+\/[a-zA-ZäöüßÄÖÜẞ]+\/KOUS'),
				re.compile(r',\/,\/\$, [a-zA-ZäöüßÄÖÜẞ]+\/so\/ADV [a-zA-ZäöüßÄÖÜẞ]+\/[a-zA-ZäöüßÄÖÜẞ]+\/VFIN'),
				re.compile(r'[a-zA-ZäöüßÄÖÜẞ]+\/[a-zA-ZäöüßÄÖÜẞ]+\/KON [a-zA-ZäöüßÄÖÜẞ]+\/so\/ADV [a-zA-ZäöüßÄÖÜẞ]+\/[a-zA-ZäöüßÄÖÜẞ]+\/VFIN')],
		'sonst' : [],
		'soweit' : [re.compile(r'[a-zA-ZäöüßÄÖÜẞ]+\/soweit\/KOUS')],
		'zugleich' : [re.compile(r'[a-zA-ZäöüßÄÖÜẞ]+\/[a-zA-ZäöüßÄÖÜẞ]+\/V[*]+ [a-zA-ZäöüßÄÖÜẞ]+\/[a-zA-ZäöüßÄÖÜẞ]+\/KON [a-zA-ZäöüßÄÖÜẞ]+\/zugleich\/ADV'),
					  re.compile(r'[a-zA-ZäöüßÄÖÜẞ]+\/zugleich\/ADV')]
		}

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

				# DISAMBIGUATION.
				zeros_to_delete = []
				ones_to_delete = []
				twos_to_delete = []
				# Iterate over DC matches associated with current Tweet object.
				for x in t.dcs:
					# If DC occurance is cited as ambiguous.
					if x[1] == True:
						# For each Schneider:
						for j in range(len(schneiders)):

							# HANDLING FOR SCHNEIDERS TYPE '0'.
							if schneiders[j][1] == 0:
								if ( x[0].part_one[0].encode("utf8") == schneiders[j][0] ) and ( 200-x[2] / float(200) ) >= zeros_limit:
									### COMMENT OUT AFTER TESTING ###									
									print "deleting type 0 discourse connective occurance %s (not a connective)!" % schneiders[j][0]
									###		
									zeros_to_delete.append(x)
								
							# HANDLING FOR SCHNEIDERS TYPE '1'.
							# Delete ambiguous cases if pos tag matches.
							if schneiders[j][1] == 1:								
								for k in instances:
									if schneiders[j][0] == k:
										if instances[k][1] in schneiders[j][2]:
											### COMMENT OUT AFTER TESTING ###
											print "deleting type 1 discourse connective occurance %s (not a connective)!" % schneiders[j][0]
											###
											ones_to_delete.append(x)											

							# HANDLING FOR SCHNEIDERS TYPE '2'.
							# Delete ambiguous cases if no exception found
							# (should be most).
							if schneiders[j][1] == 2:
								context_found = False
								for k in contexts[schneiders[j][0]]:
									if re.search(k, line):
										context_found = True
								if context_found == False:
									### COMMENT OUT AFTER TESTING ###
									#print "deleting type 2 discourse connective occurance %s (not a connective)!" % schneiders[j][0]
									###
									twos_to_delete.append(x)

				### COMMENT OUT AFTER TESTING ###
				print len(t.dcs)
				###
				for item in zeros_to_delete:
					try: 
						t.dcs.remove(item)	
					except:
						pass	
				for item in ones_to_delete:
					try: 
						t.dcs.remove(item)	
					except:
						pass		
				for item in twos_to_delete:
					try: 
						t.dcs.remove(item)	
					except:
						pass

				### COMMENT OUT AFTER TESTING ###		
				print len(t.dcs)
				print "-----"
				###

		yield t

