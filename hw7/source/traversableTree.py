# Mike Roylance - roylance@uw.edu
import nltk

class TraversableTree:
	def __init__(self, tree, parent, rules):
		self.tree = tree
		self.parent = parent
		self.children = []

		self.items = []
		self.pos = str(self.tree.node)

		self.gender = ""
		self.number = ""
		self.isPronoun = False
		self.hasPronouns = False

		self.setItems()
		self.setIsPronoun(rules)
		self.determinePlurality(rules)
		self.determineGender(rules)

		self.processChildren(rules)

	def processChildren(self, rules):
		for child in self.tree:
			# only want to process other tree
			if isinstance(child, nltk.Tree):
				newChild = TraversableTree(child, self, rules)
				self.children.append(newChild)

	def setItems(self):
		for production in self.tree.productions():
			if production.is_lexical():
				self.items.append(production)

	def setIsPronoun(self, rules):
		if self.pos in rules.acceptablePronouns:
			self.isPronoun = True
		#	self.hasPronouns = True
			return

		# for item in self.items:
		#	if str(item.lhs()) in rules.acceptablePronouns:
		#		self.hasPronouns = True
		#		return

		self.isPronoun = False

	def determinePlurality(self, rules):
		single = "sg"
		plural = "pl"

		if (self.pos in rules.pluralPartsOfSpeech):
			self.number = plural
			return

		for item in self.items:
			# check rhs first
			for terminalProduction in item.rhs():
				key = str(terminalProduction)

				if key in rules.pluralPartsOfSpeech:
					self.number = plural
					return
				elif key in rules.singlePartsOfSpeech:
					self.number = single
					return

			# then lhs
			key = str(item.lhs())
			if key in rules.pluralPartsOfSpeech:
				self.number = plural
				return
			elif key in rules.singlePartsOfSpeech:
				self.number = single
				return
		
		self.number = single

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

	def printTree(self):
		return str(self.tree.pprint(margin=500))

	def printItems(self):
		strBuilder = ""
		for item in self.items:
			for terminalProduction in item.rhs():				
				strBuilder = strBuilder + " " + str(terminalProduction)

		return strBuilder.strip()