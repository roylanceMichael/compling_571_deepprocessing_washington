# Mike Roylance - roylance@uw.edu
import sys
import nltk
import hobbs

# method for handling the second sentence found in a pair
def handleWhenSecondSentence(firstSentence, secondSentence, parser):
	# tokenize the sentences
	firstTokenizedSentence = nltk.word_tokenize(firstSentence)
	secondTokenizedSentence = nltk.word_tokenize(secondSentence)

	# parse them
	firstTrees = parser.nbest_parse(firstTokenizedSentence)
	secondTrees = parser.nbest_parse(secondTokenizedSentence)

	# verify correct parses
	if len(firstTrees) == 0 or len(secondTrees) == 0:
		print 'invalid parse!'
		print firstTokenizedSentence
		print secondTokenizedSentence
		return

	# instantiate hobbs logic
	hobbsInst = hobbs.Hobbs(firstTrees[0], secondTrees[0])
	hobbsInst.process()

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
			handleWhenSecondSentence(sentenceList[0], strippedSentence, parser)
			sentenceList = []

		# read new sentence
		sentence = sentenceFileStream.readline()

if __name__ == '__main__':
        main()