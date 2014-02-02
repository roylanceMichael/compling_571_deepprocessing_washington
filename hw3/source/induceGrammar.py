import nltk

class InduceGrammar:
	def __init__(self):
		self.foundGrammar = {}
		self.probCfg = {}

	def createProbCfg(self):

		self.probCfg = {}

		for lhs in self.foundGrammar:
			
			totalCount = 0
			for rhs in self.foundGrammar[lhs]:
				totalCount = totalCount + self.foundGrammar[lhs][rhs]

			# create dictionary now
			
			self.probCfg[lhs] = {}
			
			for rhs in self.foundGrammar[lhs]:
				self.probCfg[lhs][rhs] = float(self.foundGrammar[lhs][rhs]) / totalCount

	def getGrammar(self):
		return self.foundGrammar

	def getProbCfg(self):
		return self.probCfg

	def readSentence(self, sent):
		rootTree = nltk.Tree.parse(sent)

		prods = rootTree.productions()

		for prod in prods:

			lhs = str(prod.lhs())
			rhs = prod.rhs()

			if lhs in self.foundGrammar:
				# add count to rhs dict
				self.addRhs(self.foundGrammar[lhs], rhs)
			else:
				# create new lhs dict
				newLhsDict = {}
				self.addRhs(newLhsDict, rhs)
				self.foundGrammar[lhs] = newLhsDict

	def addRhs(self, lhsDict, rhs):
		strRhsTuple = self.convertRhsToStr(rhs)

		if strRhsTuple in lhsDict:
			lhsDict[strRhsTuple] = lhsDict[strRhsTuple] + 1
		else:
			lhsDict[strRhsTuple] = 1

	def convertRhsToStr(self, rhs):
		items = []
		
		for item in rhs:
			items.append(str(item))

		return tuple(items)
