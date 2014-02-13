# Mike Roylance - roylance@uw.edu
import sys
import nltk
import parseResult

def main():
	# arg variables
	grammarFile = sys.argv[1]
	sentenceFile = sys.argv[2]

	# create the parseResult builder
	builder = parseResult.ParseResult(grammarFile)

	# read in the example sentences
	sentenceFileStream = open(sentenceFile)
	sentence = sentenceFileStream.readline()

	# print out each sentence
	while sentence:
		print builder.buildAndPrint(sentence)
		sentence = sentenceFileStream.readline()

if __name__ == '__main__':
        main()