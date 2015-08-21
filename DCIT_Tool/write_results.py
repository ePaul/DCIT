##!/usr/bin/env python
## -*- coding: utf-8 -*-
##
## write_results.py
## Authors: J. Grasso & C. Violand
##

from bs4 import BeautifulSoup

# this only works for single tweets, not conversations!
def write_results(tweets, input_path, output_path):
	currentfile = None
	
	def write():
		if currentfile != None:
			outfile = open(output_path+currentfile+"_new.xml",'w')
			outfile.write(soup.prettify().encode("utf-8"))
			#outfile.write(unicode(soup).encode("utf-8")) # without indenting and w/ wonky newlines
			outfile.close()
	
	for t in tweets:
			
		if t.filename != currentfile:
			# every time we see a new file, write old one and open new one
			write()	
			currentfile = t.filename
			soup = BeautifulSoup(open(input_path+currentfile), "lxml")
	
		# modify soup
		results = soup.findAll("tweet", {"id" : t.id})
		# there should always be one and only one match, hence results[0]
		# add some additional attributes (just an example)
		results[0]["has_dc"] = t.has_dc()	
		results[0]["num_dcs"] = len(t.dcs)
		
		n = 1
		for d in t.dcs:
			
			results[0]["dc_location_"+str(n)] = d[2]
			n += 1
			
			
		
	write() # write the last one