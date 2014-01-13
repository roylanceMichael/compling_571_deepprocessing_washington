class SentenceTransform:
	def __init__(self, parser, tokenizer):
		self.parser = parser
		self.tokenizer = tokenizer
		self.totalParses = 0
		self.totalSentences = 0

	def parseSentence(self, sentence):
		tokenized_words = self.tokenizer.word_tokenize(sentence)

		trees = self.parser.nbest_parse(tokenized_words)

		self.totalParses = self.totalParses + len(trees)
		self.totalSentences = self.totalSentences + 1

		strBuilder = ''

		for tree in trees:
			strBuilder = strBuilder + str(tree) + '\n'

		return (strBuilder, len(trees))

	def getAverageParses(self):
		return float(self.totalParses) / float(self.totalSentences)