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

	induceInst.createProbCfg()

	# write to disk - if too large may have to do this incrementally
	fileName = 'trained.pcfg'
	try:
		os.remove(fileName)
	except OSError:
		pass

	target = open(fileName, 'w')

	for production in induceInst.getProbCfgStr():
		target.write(str(production))

if __name__ == '__main__':
        main()