```
Jessica Grasso
Universität Potsdam
MSc Program in Cognitive Systems
jgrasso@uni-potsdam.de
```
```
Clayton Violand
Universität Potsdam
MSc Program in Cognitive Systems
cvioland@uni-potsdam.de
```
# DCIT: Discourse Connectives in Twitter
## To run on (a) specific file(s):
$ python run.py a.xml b.xml
<br>
## To run on all files in ../tweets-xml/
$ python run.py glob
<br>
### Note
<b> From within ~/DCIT_Tool, the following is assumed: </b><br>
    * Dimlex.html is in ../connectives-xml/dimlex.xml.
    * Tweet files are in ../tweets-xml/.
    * POS-tagged files are in ../tweets-pos-tagged/, having the same name as the tweet file w/ extension -tagged.txt.
    * Results are written to files with extension _new.xml and saved to ../results/, which is created if it does not exist.
