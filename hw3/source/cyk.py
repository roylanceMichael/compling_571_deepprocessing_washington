import nltk
import cykNodeTuple

class Cyk:
	def __init__(self, sent, grammar, verbose=False):
		self.sent = sent
		self.sentLen = len(sent)
		self.grammar = grammar
		self.verbose = verbose
		self.workspace = []

		# build initial structure
		self.buildStructure()

	def buildStructure(self):
		for i in range(0, self.sentLen):
			subArray = []

			for j in range(0, self.sentLen - i):
				subArray.append([])

			self.workspace.append(subArray)

		# let's set the initial level
		for i in range(0, self.sentLen):
			j = 0

			for lhs in self.grammar:
				for rhs in self.grammar[lhs]:

					if len(rhs) == 1 and str(rhs[0]) == self.sent[i]:
						nonTerminal = rhs[0]
						probability = self.grammar[lhs][rhs]

						self.workspace[i][j].append(
							cykNodeTuple.CykNodeTuple(nonTerminal, probability))

	def printStructure(self):
		for item in self.workspace:
			print item