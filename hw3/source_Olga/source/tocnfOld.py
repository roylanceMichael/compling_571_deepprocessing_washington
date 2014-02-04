#author: Olga Whelan


class toCNF:
	def __init__(self):
		self.NonTerminals = []
		self.Rules = {}
		self.terminals = []
		self.newRules = {}	# rewriting new productions here
		self.index = 0
		self.startSymbol = ''


	def putDS(self, tup):
	# importing the original data structures
		self.Rules = tup[0]
		self.NonTerminals = tup[1]
		self.terminals = tup[2]
		self.startSymbol = tup[3]


	def checkRules(self):
	# method that implements the conversion
		changes = 0	# run this method as long as changes != 0
		for key in self.Rules:

			for value in self.Rules[key]:
				val = value.strip("'")
				v = val.split()
				# check if the production is too long 
				# call method checkProductionLength:
				if self.checkProductionLength(v):
					self.addToNewRules(key, [value])

				else:
				# production contains more than two components
					workingValue = value
					while len(v) > 2: 
						# LONG PRODUCTION
						changes += 1
						# call the method createDummyRule
						workingValue = self.createDummyRule(workingValue)
						self.index += 1
						
						newV = ' '.join(workingValue)
						workingValue = newV
						v = newV.split()
							
					self.addToNewRules(key, [workingValue])
		
		self.Rules = self.newRules
		self.newRules = {}

		for key in self.Rules:
			for value in self.Rules[key]:
				value.strip("'")

				if len(value.split()) == 2:
				# the production contains two components
                                        # check if non-t is combined with a term
                                        # call method checkHomogenousProduction:
                                        if self.checkHomogenousProduction(value):

						value = [value]
						self.addToNewRules(key, value)

                                        else:
					# HETEROGENOUS PRODUCTION
						changes += 1 
                                                # call method createRuleForTerminal
                                                newV = [self.createRuleForTerminal(value)]
						self.index += 1
						self.addToNewRules(key, newV)


				elif len(value.split()) == 1:
				# the production contains only one component
					# LONELY NON-TERMINAL
					# call method checkLonelyNonTerminal:
					if not self.checkLonelyNonTerminal(value):
						value = value.split()
						self.addToNewRules(key, value)

	                                else:
						changes += 1 
						getExpansionRules = self.Rules[value]
						if self.newRules.has_key(key):
							self.newRules[key] = self.newRules[key]	+ getExpansionRules
						else:
							self.newRules[key] = getExpansionRules

		self.Rules = self.newRules
		self.newRules = {}
		return changes
			

	def checkLonelyNonTerminal(self, value):
	# the check methods return True or False
		if value in self.NonTerminals:
		# it is a non-terminal! we don't want that
			return True
		else:
			return False


	def checkHomogenousProduction(self, value):
	# the check methods return True or False
		elements = value.split()
		s = 0
		if elements[0] in self.NonTerminals:
			s += 1
		if elements[1] in self.NonTerminals:
			s += 1
		if s == 2:
			return True
		else:
			return False


	def checkProductionLength(self, value):
	# the check methods return True or False
		if len(value) <= 2:
			return True
		else:
			return False


	def addToNewRules(self, key, value):
	# here I assemble new rules after conversion; the rules that already conform to the format go here directly
		if self.newRules.has_key(key):

                	self.newRules[key].extend(value)
                else:
                	self.newRules[key] = value


	def createRuleForTerminal(self, value):
	# find the terminal in the pair; create a new key; create a new value pair without the terminal;
	# update the rules dictionary with the new key-value pair; update the list of non-terminals
		elements = value.split()
		term = sorted(elements)[0]
		position = elements.index(term)
		# make an individual non-terminal name
		keyword = term.strip('"')

		newKey = self.makeNewKey(keyword)

		term = [term]
		self.addToNewRules(newKey, term)

		self.NonTerminals.append(newKey)

		if position == 0:
			newValue = str(newKey) + ' ' + str(elements[1])
			
		else:		
			newValue = str(elements[0]) + ' ' + str(newKey)
		return newValue


	def makeNewKey(self, term):
	# makes an individual key for a terminal mixed with non-terminal
		k = 'X' + term
		return k


	def createDummyRule(self, value):
		elements = value.split()
		
		keyword = ''.join(elements[0:2])
		newKey = self.makeNewKey(keyword)

		newKeyVal = [' '.join(elements[0:2])]

		self.addToNewRules(newKey, newKeyVal)

		self.NonTerminals.append(newKey)
		
		newKey = [newKey]
		newValue = newKey + elements[2:]
		newVal = ' '.join(newValue)
		newV = [newVal]

		return newV


	def formatCNF(self):
		strBuilder = ""
		for key in sorted(self.Rules):
			for value in self.Rules[key]:
				strBuilder = strBuilder + key + " -> " + value + '\n'
			strBuilder = strBuilder + "\n"
		return strBuilder


        def getDS(self):
                return (self.Rules, self.startSymbol)
