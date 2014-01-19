import nltk
class Production:
	def __init__(self):
		self.lhs = ""
		self.rhs = []

	def getLhs(self):
		return self.lhs

	def setLhs(self, value):
		self.lhs = value

	def getRhs(self):
		return self.rhs

	def addToRhs(self, value):
		self.rhs.append(value)

def factory(contextFreeGrammar):
	grammar = nltk.parse_cfg(contextFreeGrammar)

	print dir(grammar)
	print 'cnf ' + str(grammar.is_chomsky_normal_form())
	print type(grammar)
	
	productions = grammar.productions()
	
	newProductions = []

	for i in range(0, len(productions)):
		newProduction = Production()
		newProduction.setLhs(str(productions[i].lhs()))

		rhsTuple = productions[i].rhs()
		for j in range(0, len(rhsTuple)):
			newProduction.addToRhs(str(rhsTuple[j]))

		newProductions.append(newProduction)

	return newProductions