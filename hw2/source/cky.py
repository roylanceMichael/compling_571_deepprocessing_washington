class Cky:
	def __init__(self, sentence, grammar, verbose=False):
		self.verbose = verbose
		self.sentence = sentence
		self.sentenceLen = len(sentence)
		self.grammar = grammar
		self.workspace = []

		# build triangular table
		self.buildStructure()

	def printStructure(self):
		for item in self.workspace:
			print item

	def log(self, message):
		if(self.verbose):
			print message

	def isInGrammar(self):
		firstLen = len(self.workspace[0])

		return len(self.workspace[0][firstLen - 1]) > 0

	def buildStructure(self):
		for i in range(0, self.sentenceLen):
			subArray = []

			for j in range(0, self.sentenceLen - i):
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

	def executeAlgorithm(self):
		self.log('')
		for level in range(1, self.sentenceLen):

			for i in range(0, self.sentenceLen):

				self.log(str(i) + ' ' + str(level) + ' ' + str(len(self.workspace[i])))

				if level >= len(self.workspace[i]):
					continue

				acceptablePairs = self.getAcceptablePairs(i, level)

				self.log(acceptablePairs)

				for production in self.grammar.productions():

					lhs = production.lhs()
					rhs = production.rhs()

					if len(rhs) == 1:
						continue

					for pair in acceptablePairs:

						self.log('comparing ' + str(pair[0]) + ' ' + str(pair[1]) + ' to ' + str(rhs[0]) + ' ' + str(rhs[1]))

						if str(pair[0]) == str(rhs[0]) and str(pair[1]) == str(rhs[1]):
							self.log('success with ' + str(lhs))
							self.workspace[i][level].append(str(lhs))

	def getAcceptablePairs(self, rowIndex, level):
		# level means where we should start in the index
		pairs = []

		for i in range(0, level):
			firstComparison = (rowIndex, level - i - 1)
			secondComparison = (rowIndex + level - i, i)

			firstItems = self.workspace[firstComparison[0]][firstComparison[1]]

			if (secondComparison[0] < self.sentenceLen and 
				secondComparison[1] < len(self.workspace[secondComparison[0]])):

				secondItems = self.workspace[secondComparison[0]][secondComparison[1]]

				for firstItem in firstItems:
					for secondItem in secondItems:
						pairs.append((firstItem, secondItem))

		return pairs