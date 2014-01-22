import nltk
class CfgTransform:
	def __init__(self, cfg):
		self.grammar = nltk.parse_cfg(cfg)
		self.terminalToNonTerminal = {}
		self.nonTerminal = {}
		self.seed = 0

	def buildCnf(self):
		for production in self.grammar.productions():
			lhs = production.lhs()
			lhsSymbol = str(lhs)

			rhs = production.rhs()

			for i in range(0, len(rhs)):
				item = rhs[i]

				if nltk.grammar.is_terminal(item):
					terminalSymbol = str(item)

					if not terminalSymbol in self.terminalToNonTerminal:
						newId = self.generateNewId(lhsSymbol)


						self.terminalToNonTerminal[terminalSymbol] = newId

	def generateNewId(self, existingNonTerminal):
		if not existingNonTerminal in self.nonTerminal:
			self.nonTerminal[existingNonTerminal] = None
			return existingNonTerminal

		tempNonTerminal = existingNonTerminal
		incrementor = 0
		while tempNonTerminal in self.nonTerminal:
			incrementor = incrementor + 1
			tempNonTerminal = existingNonTerminal + str(incrementor)

		self.nonTerminal[tempNonTerminal] = None
		return tempNonTerminal

	def handleProduction(self, production):
		rhs = production.rhs()


	def handleAllTerminals(self, production):
		rhs = production.rhs()



