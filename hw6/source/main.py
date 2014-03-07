# Mike Roylance - roylance@uw.edu
import sys
import nltk
import resnik
import relationalWordBuilder
import icGenerator
import utils
from nltk.corpus import wordnet as wn

def handleResnik(resnikInstance, wsdContextsFile, handleItem):
	wsdContextsStream = open(wsdContextsFile)
	wsdContextsLine = wsdContextsStream.readline()

	while wsdContextsLine:
		for item in resnikInstance.processLine(wsdContextsLine):
			handleItem(item)
		
		wsdContextsLine = wsdContextsStream.readline()

def main():
	# arg variables
	informationContentMeasureFile = sys.argv[1]
	wsdContextsFile = sys.argv[2]

	# optional - compute own ic measure
	# load the information content measure
	ic = nltk.corpus.wordnet_ic.ic(informationContentMeasureFile)
	resnikInstance = resnik.Resnik(ic)

	# definining closure function
	def printLineItem(item):
		print item,

	handleResnik(resnikInstance, wsdContextsFile, printLineItem)

	# EXTRA CREDIT
	# get a list of all the words and their contexts (again)
	words = relationalWordBuilder.RelationalWordBuilder(wsdContextsFile).getAllWords()

	# custom ic file
	brownCorpusLocation = sys.argv[3]

	# new file location
	newIcFile = sys.argv[4]
	newResults = sys.argv[5]

	icGen = icGenerator.IcGenerator(words, brownCorpusLocation, newIcFile).generate()
	newIc = utils.buildIc(newIcFile)
	
	newResnik = resnik.Resnik(newIc)

	with open(newResults, 'w') as newFile:
		# handle closure
		def writeToFile(item):
			newFile.write(item)

		handleResnik(resnikInstance, wsdContextsFile, writeToFile)


if __name__ == '__main__':
        main()