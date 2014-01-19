import production

class OriginalGrammar:
	def __init__(self, contextFreeGrammar):
		self.contextFreeGrammar = contextFreeGrammar
		self.productions = production.factory(contextFreeGrammar)
		self.cnfProductions = []

	def convertFirstStep(self):
		self.cnfProductions.append()