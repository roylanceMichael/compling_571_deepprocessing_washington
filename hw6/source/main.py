# Mike Roylance - roylance@uw.edu
import sys
import nltk
import resnik
from nltk.corpus import wordnet as wn

def main():
	# arg variables
	informationContentMeasureFile = sys.argv[1]
	wsdContextsFile = sys.argv[2]

	# optional - compute own ic measure
	# load the information content measure
	ic = nltk.corpus.wordnet_ic.ic(informationContentMeasureFile)
	resnikInstance = resnik.Resnik(ic)

	wsdContextsStream = open(wsdContextsFile)
	wsdContextsLine = wsdContextsStream.readline()

	while wsdContextsLine:
		for item in resnikInstance.processLine(wsdContextsLine):
			print item,
		
		wsdContextsLine = wsdContextsStream.readline()

if __name__ == '__main__':
        main()