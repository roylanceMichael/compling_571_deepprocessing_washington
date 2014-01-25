import nltk
class CfgToCnfBuilder:
	def __init__(self, cfgGrammar):
		self.grammar = nltk.parse_cfg(cfgGrammar)
		self.newProductions = []
		self.seed = 1

	def generateKey(self):
		key = "X" + str(self.seed)
		self.seed = self.seed + 1
		return key

	def getGrammar(self):
		return self.grammar

	def getNewProductions(self):
		return self.newProductions

	def build(self):
		self.newProductions = []

		for production in self.grammar.productions():
			if self.isCnf(production):
				self.newProductions.append(production)
			else:
				self.handleProductionWithTerminals(production)

	def handleProductionWithTerminals(self, production):
		# this production needs to be split up
		rhs = production.rhs()

		newItemList = []
		newProductions = []

		for item in rhs:
			if nltk.grammar.is_nonterminal(item):
				# add non terminal to list
				newItemList.append(item)
			else:
				# create new LHS and append
				newLhsKey = self.generateKey()
				lhs = nltk.Nonterminal(newLhsKey)
				newItemList.append(lhs)

				# create new RHS and add to productions
				rhs = tuple([ item ])
				newProduction = nltk.grammar.Production(lhs, rhs)
				newProductions.append(newProduction)

		newRootLhs = production.lhs()
		newRootRhs = tuple(newItemList)

		newRootProduction = nltk.grammar.Production(newRootLhs, newRootRhs)

		self.newProductions.append(newRootProduction)

		for production in newProductions:
			self.newProductions.append(production)

	def isCnf(self, production):
		# is the length 2 and both non terminal?
		rhs = production.rhs()

		if (len(rhs) == 2 and 
			nltk.grammar.is_nonterminal(rhs[0]) and 
			nltk.grammar.is_nonterminal(rhs[1])):
			return True

		if (len(rhs) == 1 and 
			nltk.grammar.is_terminal(rhs[0])):
			return True

		return False