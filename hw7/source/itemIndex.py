class ItemIndex:
	def __init__(self, item, pos, subTree, rootTree, index, rules):
		self.item = item
		self.pos = pos
		self.subTree = subTree
		self.rootTree = rootTree
		self.index = index

		# number and gender agreement
		self.plurality = ""
		self.gender = ""

		# set them now
		self.determinePlurality(rules)
		self.determineGender(rules)

	def determinePlurality(self, rules):
		if (self.pos in rules.pluralPartsOfSpeech or
			self.item in rules.pluralPartsOfSpeech):
			self.plurality = "pl"
		else:
			self.plurality = "sg"

	def determineGender(self, rules):
		if (self.pos in rules.malePartsOfSpeech or 
			self.pos in rules.malePartsOfSpeech):
			self.gender = "m"

		elif (self.pos in rules.femalePartsOfSpeech or 
				self.pos in rules.femalePartsOfSpeech):
			self.gender = "f"

		else:
			self.gender = "u"

	def __str__(self):
		return "%s %s %s %s" % (self.item, self.pos, self.index, self.subTree)