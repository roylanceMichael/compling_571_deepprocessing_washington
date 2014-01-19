import nltk

class OriginalGrammar:
	def __init__(self, contextFreeGrammar):
		self.contextFreeGrammar = contextFreeGrammar
		self.productions = nltk.parse_cfg(contextFreeGrammar).productions()

	def getProduction(self, productionIdx):
		productionHash = {}

		production = self.productions[productionIdx]
		
		productionHash['lhs'] = str(production.lhs())

		rhsTuple = production.rhs()
		rhsList = []

		for i in range(0, len(rhsTuple)):
			rhsList.append(str(rhsTuple[i]))

		productionHash['rhs']= rhsList

		return productionHash