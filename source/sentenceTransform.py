# Mike Roylance - roylance@uw.edu
class SentenceTransform:
	def __init__(self, parser, tokenizer):
		self.parser = parser
		self.tokenizer = tokenizer
		self.totalParses = 0
		self.totalSentences = 0

	def parseSentence(self, sentence):
		# tokenize words
		tokenized_words = self.tokenizer.word_tokenize(sentence)

		# build the trees from the words
		trees = self.parser.nbest_parse(tokenized_words)

		# increment total parses and sentences
		self.totalParses = self.totalParses + len(trees)
		self.totalSentences = self.totalSentences + 1

		# build a string to return
		strBuilder = ''

		for tree in trees:
			strBuilder = strBuilder + str(tree) + '\n'

		return (strBuilder, len(trees))

	# calculate average parses
	def getAverageParses(self):
		return float(self.totalParses) / float(self.totalSentences)