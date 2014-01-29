class Cky:
	def __init__(self, sentence, grammar):
		self.sentence = sentence
		self.sentenceLen = len(sentence)
		self.grammar = grammar
		self.workspace = []

		# build triangular table
		self.buildStructure()

	def printStructure(self):
		for item in self.workspace:
			print item

	def buildStructure(self):
		for i in range(0, self.sentenceLen):
			subArray = []

			for j in range(0, self.sentenceLen - i + 1):
				subArray.append([])

			self.workspace.append(subArray)

		# let's set the initial level
		for i in range(0, self.sentenceLen):
			j = 0

			for production in self.grammar.productions():

				lhs = str(production.lhs())
				rhs = production.rhs()

				if len(rhs) == 1 and str(rhs[0]) == self.sentence[i]:
					self.workspace[i][j].append(lhs)

	def getAcceptablePairs(self, rowIndex, level):
		# level means where we should start in the index
		pairs = []

		for i in range(0, level):

			for lookAheadIndex in range(rowIndex + 1, rowIndex + level + 1):

				if lookAheadIndex >= self.sentenceLen:
					break

				for j in range(0, level):
					if i + j > level:
						break

					originalProductions = self.workspace[rowIndex][i]
					futureProductions = self.workspace[lookAheadIndex][j]

					for origProd in originalProductions:
						for futureProd in futureProductions:
							pairs.append((origProd, futureProd))

		return pairs


			



