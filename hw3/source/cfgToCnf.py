import nltk
import productionBuilder 

class CfgToCnf:
	def __init__(self, productions):
		self.pb = productionBuilder.ProductionBuilder()

		self.originalProductions = productions
		self.terminalTransformProductions = []
		self.nonTerminalTransformProductions = []
		self.singleNonTerminalTransformProductions = []

	def getFinalProductions(self):
		return self.singleNonTerminalTransformProductions

	def build(self):
		self.nonTerminalTransformProductions = []
		self.terminalTransformProductions = []

		# splitting into three steps for transparency
		for production in self.originalProductions:
			if self.isCnf(production):
				self.terminalTransformProductions.append(production)
			else:
				self.handleProductionWithTerminals(production)

		for production in self.terminalTransformProductions:
			if self.isCnf(production):
				self.nonTerminalTransformProductions.append(production)
			else:
				self.handleProductionWithNonTerminals(production)

		for production in self.nonTerminalTransformProductions:
			if self.isCnf(production):
				self.singleNonTerminalTransformProductions.append(production)
			else:
				self.handleSingleNonTerminals(production, self.nonTerminalTransformProductions)

	def handleSingleNonTerminals(self, production, productions):
		# this production has just one non terminal
		rhs = production.rhs()

		if len(rhs) == 1 and nltk.grammar.is_nonterminal(rhs[0]):

			childCnfProductions = self.findChildCnfProduction(production, productions)

			lhs = production.lhs()

			for childProd in childCnfProductions:
				rhs = childProd.rhs()
				prod = self.pb.buildNormal(lhs, rhs)
				self.singleNonTerminalTransformProductions.append(prod)

	def findChildCnfProduction(self, production, productions):
		# note, this function will only be accessed
		# when there is one rhs in the production
		nonTermSym = str(production.rhs()[0])

		foundProds = []

		for otherProds in productions:
			lhSym = str(otherProds.lhs())

			rhs = otherProds.rhs()

			if lhSym == nonTermSym:

				if self.isCnf(otherProds):
					foundProds.append(otherProds)
					
			 	if len(rhs) == 1:
			 		
			 		childProds = self.findChildCnfProduction(otherProds, productions)

			 		foundProds = foundProds + list(childProds)

		return foundProds

	def handleProductionWithNonTerminals(self, production):
		# this production has more than two non terminals
		workspace = list(production.rhs())

		# we'll be working from the end
		workspace.reverse()

		newProductions = []

		# if rhs is greater than 2
		while len(workspace) > 2:
			firstItem = workspace.pop()
			secondItem = workspace.pop()

			rhs = (firstItem, secondItem)
			newProduction = self.pb.build(rhs)

			workspace.append(newProduction.lhs())
			newProductions.append(newProduction)

		# reverse back
		workspace.reverse()

		newRootLhs = production.lhs()
		newRootRhs = tuple(workspace)

		newRootProduction  = self.pb.buildNormal(newRootLhs, newRootRhs)

		newProductions.insert(0, newRootProduction)

		for production in newProductions:
			self.nonTerminalTransformProductions.append(production)

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
				# create new RHS and add to productions
				rhs = tuple([ item ])
				newProduction = self.pb.build(rhs)
				newProductions.append(newProduction)

				# add lhs to current list
				newItemList.append(newProduction.lhs())

		newRootLhs = production.lhs()
		newRootRhs = tuple(newItemList)

		newRootProduction = self.pb.buildNormal(newRootLhs, newRootRhs)

		self.terminalTransformProductions.append(newRootProduction)

		for production in newProductions:
			self.terminalTransformProductions.append(production)

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