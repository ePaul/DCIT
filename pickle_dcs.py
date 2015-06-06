import sys
import pickle
from DiscourseConnective import DiscourseConnective
from bs4 import BeautifulSoup

def pickle_dcs():

	try:
		path=sys.argv[1]
		print('\tUsing file ' + path + '...')
		
	except:
		print "Exiting, problem with file."
		return

	soup = BeautifulSoup(open(path), "xml")

	# Creates a list of DiscourseConnective objects.
	print "\tCreating list of DiscourseConnective objects..."
	dcons = []
	for i in soup.find_all('entry'):
		dcon = DiscourseConnective(i)
		dcons.append(dcon)
	
	# pickle the connectives
	print "\tPickling..."

	with open('dcs.pickle', 'wb') as handle:
		pickle.dump(dcons, handle)



pickle_dcs()