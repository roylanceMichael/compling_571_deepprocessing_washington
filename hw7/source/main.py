# Mike Roylance - roylance@uw.edu
import sys
import nltk
import hobbs
import utils

def main():
	# arg variables
	grammarFile = "file:" + sys.argv[1]
	sentenceFile = sys.argv[2]

	# create grammar
	grammar = nltk.data.load(grammarFile)
	parser = nltk.parse.EarleyChartParser(grammar)
	
	# read in the sentences
	sentenceList = []
	sentenceFileStream = open(sentenceFile)
	sentence = sentenceFileStream.readline()

	while sentence:
		# first, strip sentence so we can detect empty string
		strippedSentence = sentence.strip()
		# add if length is 0
		if len(sentenceList) == 0 and len(strippedSentence) > 0:
			sentenceList.append(strippedSentence)
		# process if length is 1
		elif len(sentenceList) == 1 and len(strippedSentence) > 0:
			trees = utils.buildTreesFromSentences(sentenceList[0], strippedSentence, parser)

			hobbsInst = hobbs.Hobbs(trees[0], trees[1])
			hobbsInst.process()

			sentenceList = []

		# read new sentence
		sentence = sentenceFileStream.readline()

if __name__ == '__main__':
        main()