# Mike Roylance - roylance@uw.edu
import nltk

class ParseResult:
	# constructor
	def __init__(self, featureGrammarFile):
		self.parser = nltk.load_parser("file:" + featureGrammarFile)

	# build the sentence tree
	def build(self, sentence):
		tokenizedSentence = nltk.word_tokenize(sentence)
		return self.parser.nbest_parse(tokenizedSentence)

	# build the sentence tree and print out, if it exists
	def buildAndPrint(self, sentence):
		result = self.build(sentence)

		if len(result) > 0:
			return str(result[0].pprint(margin=500))
		return ''