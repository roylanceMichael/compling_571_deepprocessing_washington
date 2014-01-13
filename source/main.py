import nltk
import sys
import re
import sentenceTransform

def main():
	# build grammar file url
	grammarFile = "file:" + sys.argv[1]
	sentenceFile = sys.argv[2]

	# read in grammar
	grammar = nltk.data.load(grammarFile)
	
	# build chart parser
	parser = nltk.parse.EarleyChartParser(grammar)

	# create transformer
	sentTransform = sentenceTransform.SentenceTransform(parser, nltk)

	# read in sentences
	input_stream = open(sentenceFile)

	line = input_stream.readline()

	while(line):
		dataTuple = sentTransform.parseSentence(line.strip().lower())

		print dataTuple[0]
		print dataTuple[1]

		line = input_stream.readline()

	print sentTransform.getAverageParses()

	# for each sentence
	# 	delimit by space, print out bracked sentence
	#	print out number of parses
	# end, print out average

if __name__ == '__main__':
        main()