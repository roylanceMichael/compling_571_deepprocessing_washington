# Mike Roylance - roylance@uw.edu
import sys
import nltk

def main():
	# const variables
	sem = "SEM"

	# arg variables
	grammarFile = sys.argv[1]
	sentenceFile = sys.argv[2]

	# create FeatureChartParser parser
	parser = nltk.load_parser('file:' + grammarFile, trace=0)

	# read in the example sentences
	sentenceFileStream = open(sentenceFile)
	sentence = sentenceFileStream.readline()

	# print out each sentence
	while sentence:
		tokenizedSent = nltk.word_tokenize(sentence)
		trees = parser.nbest_parse(tokenizedSent)

		if len(trees) > 0:
			print trees[0].node[sem].simplify()
			
		sentence = sentenceFileStream.readline()

if __name__ == '__main__':
        main()