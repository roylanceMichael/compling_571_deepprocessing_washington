# Mike Roylance - roylance@uw.edu
import nltk
import parseResult

def main():
	# arg variables
	grammarFile = sys.argv[1]
	sentenceFile = sys.argv[2]

	# read in the original grammar
	input_stream = open(grammarFile)
	grammarText = input_stream.read()
	input_stream.close()

	# create the parseResult builder
	builder = parseResult.ParseResult(grammarText)

	# read in the example sentences
	sentenceFileStream = open(sentenceFile)
	sentence = sentenceFileStream.readline()

	while sentence:
		print builder.build(sentence)

if __name__ == '__main__':
        main()