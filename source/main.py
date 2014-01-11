import nltk
import sys
import re

def main():
	# build grammar file url
	grammarFile = "file:" + sys.argv[1]
	sentenceFile = sys.argv[2]

	# read in grammar
	grammar = nltk.data.load(grammarFile)
	
	# build chart parser
	parser = nltk.parse.EarleyChartParser(grammar)

	# read in sentences
	input_stream = open(sentenceFile)

	line = input_stream.readline()

	while(line):
		words = nltk.word_tokenize(line.strip().lower())
		
		print words
		# print parser.nbest_parse(words)

		line = input_stream.readline()

	# for each sentence
	# 	delimit by space, print out bracked sentence
	#	print out number of parses
	# end, print out average

if __name__ == '__main__':
        main()