# DCIT
Discourse Connectives in Twitter

Jessica Grasso
Universität Potsdam
MSc Program in Cognitive Systems
jgrasso@uni-potsdam.de

Clayton Violand
Universität Potsdam
MSc Program in Cognitive Systems
charles.violand@uni-potsdam.de

It assumes dimlex.html is located at ../connectives-xml/dimlex.xml , tweet files are located at ../tweets-xml/ , and POS-tagged files have the same name with -tagged.txt extension and are located at ../tweets-pos-tagged/ .  Results are written to files with _new.xml extension and saved to ../results/ , which is created if it does not exist.

To run on (a) specific file(s):

$ python run.py a.xml b.xml

To run on all files in ../tweets-xml/

$ python run.py glob
