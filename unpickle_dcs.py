import sys
import pickle
from DiscourseConnective import DiscourseConnective

def main():
	try:
		path=sys.argv[1]		
	except:
		print "No file name given!"
		return
		
	print('\tImporting file ' + path)

	print "\tUn-pickling... "
	
	with open(path, 'rb') as handle:
		dcs = pickle.load(handle)
	  
	# then for example,
	#print dcs
		  
if __name__ == "__main__":
	main()