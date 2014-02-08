# Mike Roylance - roylance@uw.edu
import nltk

class ParseResult:
	def __init__(self, grammarStr):
		self.grammar = nltk.parse.FeatureEarlyChartParse(grammarStr)

	def build(self, sentence):
		pass