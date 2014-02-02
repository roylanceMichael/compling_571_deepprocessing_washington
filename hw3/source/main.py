import nltk
import sys
import re
import os
import induceGrammar

def main():
	# arg variables
	annotatedSentencesFile = sys.argv[1]
	sentencesFile = sys.argv[2]

	# induce grammar
	induceInst = induceGrammar.InduceGrammar()

	# read in the annotated sentences
	input_stream = open(annotatedSentencesFile)
	annotatedSentence = input_stream.readline()

	while annotatedSentence:
		induceInst.readSentence(annotatedSentence)
		annotatedSentence = input_stream.readline()

	input_stream.close()

	# print out to console
	grammarDict = induceInst.getGrammar()

	for key in grammarDict:
		print grammarDict[key]

if __name__ == '__main__':
        main()