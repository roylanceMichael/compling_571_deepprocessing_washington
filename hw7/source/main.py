# Mike Roylance - roylance@uw.edu
import sys
import nltk
import hobbs

def handleWhenSecondSentence(firstSentence, secondSentence, parser):
	firstTokenizedSentence = nltk.word_tokenize(firstSentence)
	secondTokenizedSentence = nltk.word_tokenize(secondSentence)

	firstTrees = parser.nbest_parse(firstTokenizedSentence)
	secondTrees = parser.nbest_parse(secondTokenizedSentence)

	if len(firstTrees) == 0 or len(secondTrees) == 0:
		print 'invalid parse!'
		print firstTokenizedSentence
		print secondTokenizedSentence
		return

	hobbsInts = hobbs.Hobbs(firstTrees[0], secondTrees[0])

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
		strippedSentence = sentence.strip()
		if len(sentenceList) == 0 and len(strippedSentence) > 0:
			sentenceList.append(strippedSentence)
		elif len(sentenceList) == 1 and len(strippedSentence) > 0:
			handleWhenSecondSentence(sentenceList[0], strippedSentence, parser)
			sentenceList = []

		sentence = sentenceFileStream.readline()

if __name__ == '__main__':
        main()