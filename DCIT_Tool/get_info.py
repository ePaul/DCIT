#!/usr/bin/env python

# get_info.py
# Authors: Jessica E. Grasso & C. Clayton Violand

from heapq import nlargest
from operator import itemgetter

class Info():

	def __init__(self, dcons):
		self.tweets = 0
		# number of tweets seen
		self.dcs_found = 0
		# number of discourse connectives
		self.tweets_with_dcs = 0
		# how many tweets contain at least one discourse connective
		
		self.continuous = 0
		# continuous single (aber)
		self.discontinuous = 0
		# continuous phrasal (abgesehen davon)
		
		# how many of the above are ambiguous
		self.continuous_ambi = 0
		self.discontinuous_ambi = 0
		
		# create dictionaries of continuous, discontinuous, and ambiguous DCs to keep count
		self.continuous_dict = {}
		self.discontinuous_dict = {}
		self.ambiguous_dict = {}
		
		# populate dictionaries
		for dc in dcons:
			if dc.sep == "cont":
				self.continuous_dict[dc] = 0
			if dc.sep == "discont":
				self.discontinuous_dict[dc] = 0
			if dc.ambi == "1":
				self.ambiguous_dict[dc] = 0
		
	def ratio(self):
		# returns ratio of tweets with at least one DC to total tweets
		return float(self.tweets_with_dcs) / float(self.tweets) 
		
	def ambiguous(self):
		# returns count of ambiguous DCs
		return self.continuous_ambi + self.discontinuous_ambi
		
	def mostcommon(self, n, which_kind):
		num = n
		print "\n--------------------------------------------------------------------\n"
		if which_kind == "continuous":
			#num = int(len(self.continuous_dict) * (float(percent)/100))
			print "Printing top " + str(n) + " continuous connectives:" #, which is " + str(num) + " items:"
			
			for key, freq in nlargest(num, self.continuous_dict.iteritems(), key=itemgetter(1)):
				print "\t", key.part_one[0], "occurs ", self.continuous_dict[key], " times, which is ", float(self.continuous_dict[key])/float(self.continuous)*100, " percent."
			
		elif which_kind == "discontinuous":
			#num = int(len(self.discontinuous_dict) * (float(percent)/100))
			print "Printing top " + str(n) + " discontinuous connectives:" #, which is " + str(num) + " items:"	
			
			for key, freq in nlargest(num, self.discontinuous_dict.iteritems(), key=itemgetter(1)):
				print "\t", key.part_one[0], " ... ", key.part_two[0], "occurs ", self.discontinuous_dict[key], " times, which is ", float(self.discontinuous_dict[key])/float(self.discontinuous)*100, " percent."
			
		elif which_kind == "ambiguous":
			#num = int(len(self.ambiguous_dict) * (float(percent)/100))
			print "Printing top " + str(n) + " ambiguous connectives:" #, which is " + str(num) + " items:"	

			for key, freq in nlargest(num, self.ambiguous_dict.iteritems(), key=itemgetter(1)):
				print "\t", key.part_one[0], 
				if key.sep == "continuous":
					print " ... ", key.part_two[0],
				print "occurs ", self.ambiguous_dict[key], " times, which is ", float(self.ambiguous_dict[key])/float(self.ambiguous())*100, " percent."

		return

	def summary(self, flag=0, top_many=10):
		if flag == 0:
			print
			print "--SUMMARY--"
			print "--------------------------------------------------------------------"
			print		
			print "I. Pre-disambiguation: all matches."
			print "--------------------------------------------------------------------"
			print "Found %d potential Discourse Connective matches amongst %d Tweets." % (self.dcs_found, self.tweets)
			print "Found a potential Discourse Connective in %d out of %d Tweets." % (self.tweets_with_dcs, self.tweets)
			print "Potential Discourse Connective Saturation is %f." % self.ratio()
			print "--------------------------------------------------------------------"
			print "of type = 'continuous': %d " % self.continuous
			print "of type = 'discontinuous': %d " % self.discontinuous
			print "--------------------------------------------------------------------"
			print		
			print "II. Pre-disambiguation: ambiguous matches."
			print "--------------------------------------------------------------------"
			print "Found %d ambiguous cases amongst %d matches." % (self.ambiguous(), self.dcs_found)
			print "--------------------------------------------------------------------"
			print "of type = 'continuous': %d" % self.continuous_ambi
			print "of type = 'discontinuous': %d " % self.discontinuous_ambi
			print "--------------------------------------------------------------------"
			print
			print "III. Most common discourse connectives."

			self.mostcommon(top_many,"continuous")
			self.mostcommon(top_many,"discontinuous")
			self.mostcommon(top_many,"ambiguous")
				
		elif flag == 1:
			print "One!  Nothing here yet!"
		else:
			print "Some other number!  Nothing here yet!"
	
