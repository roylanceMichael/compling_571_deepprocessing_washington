class CykNodeTuple:
	def __init__(self, nonTerminal, probability):
		self.nonTerminal = nonTerminal
		self.probability = probability

	def getNonTerminal(self):
		return self.nonTerminal

	def getProbability(self):
		return self.probability