# Mike Roylance - roylance@uw.edu
import nltk

class ParseResult:
	def __init__(self, featureGrammarFile):
		self.parser = nltk.load_parser("file:" + featureGrammarFile)

	def build(self, sentence):
		tokenizedSentence = nltk.word_tokenize(sentence.lower())
		return self.parser.nbest_parse(tokenizedSentence)

	def buildAndPrint(self, sentence):
		result = self.build(sentence)

		if len(result) > 0:
			return str(result[0].pprint(margin=500))
		return ''