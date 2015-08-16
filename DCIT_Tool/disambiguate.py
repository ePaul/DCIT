#!/usr/env/python coding
# -*- coding: utf-8 -*-

# Authors: C. Clayton Violand & Jessica E. Grasso

import re
import string

def disambiguate(tweets, dcons, zeros_limit = 0.8):
	#SCHNEIDERS
	pattern = re.compile(r'[a-zA-ZäöüßÄÖÜẞ]+\/[a-zA-ZäöüßÄÖÜẞ]+\/[A-ZÄÖÜẞ]+')

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
																																						
	#contexts_for_schneider_twos	
	#contexts =	

	new_dcons = dcons
	
	for i in new_dcons:
		print i.part_one[0]
	print

	for d in new_dcons.copy():
		for s in schneiders:
			if s[1] == 0:
				if (d.part_one[0].encode("utf-8") == s[0]) and ((200-s[2]) / float(200)) >= zeros_limit :			
					print "\t\t\t\tremoving" + str(s[0])					
					new_dcons.remove(d)					

	for i in new_dcons:
		print i.part_one[0]

	
	current_file = {"name": None, "data": None}
	id_regex = re.compile(r'^\t+(\d)+\t(.*)$')
	
	def load_tagged_file(filename):
		if current_file["name"] != filename:
			data = dict()
			current_file["name"] = filename
			current_file["data"] = data
			tagged_path = "../tweets-POS_tagged/"+t.filename + "-tagged.txt"
			tagged = open(tagged_path)
			
			for line in tagged:
				match = id_regex.match(line)
				if(match):
					id = match.group(1)
					rest = match.group(2)
					data[id] = rest
		return current_file["data"]

	def loop_content(t, data):
		line = data.get(t.id)
		if(line):
				# remains unchanged
				results = re.findall(pattern,line)
				instances = {}
				for i in results:
					parts = string.split(i,'/')
					if parts[1] in instances.keys():
						continue
					else:
						instances[parts[1]] = (parts[0], parts[2])
				for j in range(len(schneiders)):					
					if schneiders[j][1] == 1:
						for k in instances:
							if schneiders[j][0] == k:
								if instances[k][1] in schneiders[j][2]:
									pass
					elif schneiders[j][2]:
						pass
		return t
	
	for t in tweets:
		data = load_tagged_file(t.filename)
		yield loop_content(t, data)
