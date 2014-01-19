import production
import uuid

class OriginalGrammar:
	def __init__(self, contextFreeGrammar):
		self.contextFreeGrammar = contextFreeGrammar
		self.productions = production.factory(contextFreeGrammar)
		self.cnfProductions = []

	def convertFirstStep(self):
		completelyNewStartVariable = str(uuid.uuid1())
		newProduction = production.Production()
		newProduction.setLhs(completelyNewStartVariable)

		self.cnfProductions.append(newProduction)

	def findStartNode(self):
		# cycle through and find first node that isn't production
		for i in range(0, len(self.productions)):
			currentProduction = self.productions[i]

			foundInRhs = False
			for j in range(0, len(self.productions)):
				compareProduction = self.productions[j]
				compareRhs = compareProduction.getRhs()

				for k in range(0, len(compareRhs)):
					if currentProduction.getLhs() == compareRhs[k]:
						foundInRhs = True
						break

				if foundInRhs:
					break

			if not foundInRhs:
				return currentProduction.getLhs()

		return None