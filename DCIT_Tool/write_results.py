#!/usr/bin/env python
# -*- coding: utf-8 -*-

# write_results.py
# Authors: C. Clayton Violand & Jessica E. Grasso

from bs4 import BeautifulSoup

def write_results(tweets, input_path, output_path):
	currentfile = None
	
	def write():
		if currentfile != None:
			outfile = open(output_path+currentfile+"_new.xml",'w')
			outfile.write(soup.prettify().encode("utf-8"))
			#outfile.write(unicode(soup).encode("utf-8")) # without indenting and w/ wonky newlines
			outfile.close()
	
	for t in tweets:
		# For D-Buggin'
		#t.print_dcs()
		if t.filename != currentfile:
			# every time we see a new file, write old one and open new one
			write()	
			currentfile = t.filename
			soup = BeautifulSoup(open(input_path+currentfile), "html")
	
		# modify soup
		
		results = soup.findAll("tweet", {"id" : t.id})
		# there should always be one and only one match, hence results[0]
		# add some additional attributes (just an example)
		results[0]["hasDC"] = t.has_dc
		results[0]["hasAmbiDC"] = t.has_ambi_dc
		
	write() # write the last one
