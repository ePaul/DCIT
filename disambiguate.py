#!/usr/bin/env python
#coding: utf-8

# get_matches.py
# Authors: C. Clayton Violand & Jessica E. Grasso

import re
import string

pattern = re.compile(r'[a-zA-ZäöüßÄÖÜẞ]+\/[a-zA-ZäöüßÄÖÜẞ]+\/[A-ZÄÖÜẞ]+')
text = open('tagged.txt').read()

results = re.findall(pattern,text)
instances = {}
for i in results:
	parts = string.split(i,'/')

	if parts[1] in instances.keys():
		
	else:
		instances[parts[1]] = (parts[0], parts[2])


# Add type 0s and finish type 2s.
schneiders = [('denn',1,['KON']),('doch',1,['KON']),('entgegen',1,['APPO','APPR']),('seit',1,['KOUS']),('seitdem',1,['KOUS']),('trotz',1,['APPR']),('während',1,['KOUS']),('wegen',1,['APPO','APPR']),('also',2,),('auch',2,),('außer',2,),('da',2,),('darum',2,),('nebenher',2,),('nur',2,),('so',2,),('sonst',2,),('soweit',2,)]

print instances

for i in range(len(schneiders)):
	if schneiders[i][1] == 1:
		for j in instances:
			if schneiders[i][0] == j:
				if instances[j][1] in schneiders[i][2]:
					print "CONNECTIVE CONFIRMED"
					print