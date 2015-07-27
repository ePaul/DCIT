#!/usr/bin/env python

# get_info.py
# Authors: Jessica E. Grasso & C. Clayton Violand

class Info():

	def __init__(self):
		self.tweets = 0
		# number of tweets seen
		self.dcs_found = 0
		# number of discourse connectives
		self.tweets_with_dcs = 0
		# how many tweets contain at least one discourse connective
		
		self.continuous = 0
		# continuous single (aber)
		self.disccontinuous = 0
		# continuous phrasal (abgesehen davon)
		
		# how many of the above are ambiguous
		self.continuous_ambi = 0
		self.discontinuous_ambi = 0
		
	def ratio(self):
		return float(self.tweets_with_dcs) / float(self.tweets) 
		
	def summary(self, flag=0):
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
			print "of type = 'continuous single': %d " % self.continuous
			print "of type = 'discontinuous': %d " % self.discontinuous
			print "--------------------------------------------------------------------"
			print		
			'''
			print "II. Pre-disambiguation: ambiguous matches."
			print "--------------------------------------------------------------------"
			print "Found %d ambiguous cases amongst %d matches." % (len(ambiguous_cases), hit_count)
			print "--------------------------------------------------------------------"
			print "of type = 'continuous single': %d " % len(ambiguous_singles)
			print "of type = 'continuous phrasal: %d" % len(ambiguous_phrasals)
			print "of type = 'discontinuous': %d " % len(ambiguous_separables)
			print "--------------------------------------------------------------------"
			print
			print "III. Ambiguity facts."
			print "--------------------------------------------------------------------"
			print "**Counts for ambiguous singles**"
			for i in facts_singles.most_common():
				print i, facts_singles[i]	
			print
			print "**Counts for ambiguous phrasals**"
			for i in facts_phrasals.most_common():
				print i, facts_phrasals[i]	
			print
			print "**Counts for ambiguous separables**"
			for i in facts_separables.most_common():
				print i, facts_separables[i]		
			'''
		
		elif flag == 1:
			print "One!  Nothing here yet!"
		else:
			print "Some other number!  Nothing here yet!"
	
