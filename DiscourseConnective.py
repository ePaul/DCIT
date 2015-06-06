#!/usr/bin/python

# Authors: C. Clayton Violand & Jessica E. Grasso

from bs4 import BeautifulSoup

class DiscourseConnective(object):

	def __init__(self, entry):
		self.name = entry.find("part").text
		self.type = entry.part["type"]
		self.ambi = entry.find("conn_d").text
		self.relation = entry.find("relation").text

		if entry.find("integr"):
			self.position = [i for i in entry.find("integr").text]
		else:
			self.position = None

		if entry.find("ordering"):
			self.ordering = [i for i in entry.find("ordering").text]
		else:
			self.ordering = None

#	def __str__(self):
#		print type(dcon.name)
#		print type(dcon.type)
#		print type(dcon.ambi)
#		print type(dcon.relation)
#		print type(dcon.position)
#		print type(dcon.ordering)
#		print

