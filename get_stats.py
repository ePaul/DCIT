#!/usr/bin/python

# get_stats.py
# Authors: C. Clayton Violand & Jessica E. Grasso
from heapq import nlargest
from operator import itemgetter

def get_stats(dcons, tuples, percent=100, mode='a',):

	# tuples is a list of tuples (tweet, discourse_connector)
	dcons_dict = dict()

	if mode=='a':
		mode_string="all"
		# use all connectives
		for dc in dcons:
			dcons_dict[dc] = 0	
	elif mode=='s':
		mode_string="single"
		# use only single connectives
		for dc in dcons:
			if dc.type == "single":
				dcons_dict[dc] = 0
	elif mode=='p':
		mode_string="phrasal"
		# use only phrasal connectives
		for dc in dcons:
			if dc.type == "phrasal":
				dcons_dict[dc] = 0	
	else:
		print "Invalid argument for mode!"
		return
	
	for t,d in tuples:
		# increment count in dictionary for each discourse connective
		dcons_dict[d] += 1
	
	# total number of dc's is the sum of all values in dictionary
	total = sum(dcons_dict.values())
	
	# super ugly nested thing!
	num = int(len(dcons_dict.keys()) * (float(percent)/100))
	
	print "\n--------------------------------------------------------------------"
	print "Printing top " + str(percent) + " percent of " + mode_string + " connectives, which is " + str(num) + " items:"
	
	
	#for key in sorted(dcons_dict, key=dcons_dict.get, reverse=True):
	#	print "\t", key.name, "occurs ", dcons_dict[key], " times, which is ", float(dcons_dict[key])/float(total)*100, " percent."
	
	for key, freq in nlargest(num, dcons_dict.iteritems(), key=itemgetter(1)):
		print "\t", key.name, "occurs ", dcons_dict[key], " times, which is ", float(dcons_dict[key])/float(total)*100, " percent."
	
	return dcons_dict