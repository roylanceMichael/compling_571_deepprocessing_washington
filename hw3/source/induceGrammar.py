import nltk
import cfgToCnf

class InduceGrammar:
	def __init__(self):
		self.foundGrammar = {}
		self.probCfg = {}
		self.terminals = {}

	def createProbCfg(self):

		self.probCfg = {}
		self.terminals = {}

		for lhs in self.foundGrammar:
			
			totalCount = 0
			for rhs in self.foundGrammar[lhs]:
				totalCount = totalCount + self.foundGrammar[lhs][rhs]

			# create dictionary now
			
			self.probCfg[lhs] = {}
			
			for rhs in self.foundGrammar[lhs]:
				# build up a reverse terminal dictionary too
				if len(rhs) == 1:
					self.terminals[rhs[0]] = lhs

				self.probCfg[lhs][rhs] = float(self.foundGrammar[lhs][rhs]) / totalCount

	def getGrammar(self):
		return self.foundGrammar

	def getProbCfg(self):
		return self.probCfg

	def getProbCfgStr(self):
		strBuilder = ""
		carriageReturn = "\n"

		for lhs in self.probCfg:

			for rhs in self.probCfg[lhs]:
				rhsStr = self.getTupleToStr(rhs)
				probability = self.probCfg[lhs][rhs]
				yield "%s -> %s [%s] %s" % (lhs, rhsStr, probability, carriageReturn)

	def getTupleToStr(self, items):
		strBuilder = ""

		for item in items:
			strBuilder = strBuilder + " " + str(item)

		return strBuilder.strip()

	def readSentence(self, sent):
		rootTree = nltk.Tree.parse(sent)

		prods = rootTree.productions()
		builder = cfgToCnf.CfgToCnf(prods)
		builder.build()

		for prod in builder.getFinalProductions():

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