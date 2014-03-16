# Mike Roylance - roylance@uw.edu

class ItemIndex:
	def __init__(self, pos, subTree, rootTree, index, rules):
		self.pos = pos
		self.items = []
		self.subTree = subTree
		self.rootTree = rootTree
		self.index = index

		# set items
		self.setItems()

		# number and gender agreement
		self.plurality = ""
		self.gender = ""

		# set them now
		self.determinePlurality(rules)
		self.determineGender(rules)

	def setItems(self):
		for production in self.subTree.productions():
			if production.is_lexical():
				self.items.append(production)

	def determinePlurality(self, rules):
		if (self.pos in rules.pluralPartsOfSpeech):
			self.plurality = "pl"
			return

		for item in self.items:
			for terminalProduction in item.rhs():
				if str(terminalProduction) in rules.pluralPartsOfSpeech:
					self.plurality = "pl"
					return

			if str(item.lhs()) in rules.pluralPartsOfSpeech:
				self.plurality = "pl"
				return
		
		self.plurality = "sg"

	def determineGender(self, rules):
		if self.pos in rules.malePartsOfSpeech:
			self.gender = "m"
			return

		for item in self.items:
			for terminalProduction in item.rhs():
				if str(terminalProduction) in rules.malePartsOfSpeech:
					self.gender = "m"
					return
		
		self.gender = "u"

	def printItems(self):
		strBuilder = ""
		for item in self.items:
			for terminalProduction in item.rhs():				
				strBuilder = strBuilder + " " + str(terminalProduction)

		return strBuilder.strip()

	def printSubTree(self):
		return self.subTree.pprint(margin=500)

	def __str__(self):
		return "%s %s %s %s %s %s" % (self.printItems(), self.gender, self.plurality, self.pos, self.index, self.subTree)