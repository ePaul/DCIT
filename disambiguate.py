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
	instances[parts[1]] = (parts[0], parts[2])

print instances
