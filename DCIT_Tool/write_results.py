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

		# add tags to the text itself marking where (potential) DCs were found
		n = 0
		text = results[0]["text"]
		tag = "DC/"
		oldindex = 0
		newtext = ""
		
		for d in sorted(t.dcs, key=lambda x:x[2]):
			if n == 0:	# first
				newtext = text[:d[2]] + tag
			else: # all others
				newtext = newtext + text[oldindex:d[2]] + tag
			n += 1
			oldindex = d[2]
		# end of string
		newtext = newtext + text[oldindex:]
		
		results[0]["text"] = newtext

	write() # write the last one