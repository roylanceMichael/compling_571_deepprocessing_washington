# Mike Roylance - roylance@uw.edu
import nltk
import sys
import re
import os
import cky
import cfgToCnfBuilder
import productionBuilder

def main():
	# arg variables
	grammarFile = sys.argv[1]
	sentenceFile = sys.argv[2]

	# read in the original grammar
	input_stream = open(grammarFile)
	grammarText = input_stream.read()
	input_stream.close()

	# convert the original grammar to CNF
	cfgBuilder = cfgToCnfBuilder.CfgToCnfBuilder(grammarText)
	cfgBuilder.build()

	# load in the CNF grammar
	cnfGrammar = cfgBuilder.getFinalProductions()

	# print out the rules of the converted grammar to a file named grammar.cnf
	fileName = 'grammar.cnf'
	try:
		os.remove(fileName)
	except OSError:
		pass

	target = open(fileName, 'w')

	for production in cnfGrammar:
		target.write(str(production))
		target.write('\n')

    # read in the example sentences
	sentenceFileStream = open(sentenceFile)
	sentences = sentenceFileStream.readlines()
	sentenceFileStream.close()

    # for each example sentence, output to a file
    #	the simple bracketed structure parse(s)
    #	the number of parses for that sentence.
	for sentence in sentences:
		tokenizedSent = nltk.word_tokenize(sentence)
		print tokenizedSent
		ckyInst = cky.Cky(tokenizedSent, cnfGrammar)
		ckyInst.executeAlgorithm()
		print ckyInst.isInGrammar()

if __name__ == '__main__':
        main()