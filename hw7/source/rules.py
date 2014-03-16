class Rules:
	def __init__(self):
		self.acceptablePronouns = {}
		self.acceptableAntecedents = {}

		self.populateAcceptablePronouns()
		self.populateAcceptableAntecedents()

	def indexAgreement(self, firstIndex, secondIndex):
		# are the two trees the same?
		if (self.areTreesEqual(firstIndex, secondIndex) and 
			self.isFirstTreeBeforeSecondTree(firstIndex)):
			return True

		return False

	def populateAcceptablePronouns(self):
		# hard coding the pronouns, as found in ../docs/grammar.cfg
		self.acceptablePronouns["PRP"] = None
		self.acceptablePronouns["PossPro"] = None

	def populateAcceptableAntecedents(self):
		self.acceptableAntecedents["S"] = None
		self.acceptableAntecedents["NP"] = None

	def areTreesEqual(self, firstTree, secondTree):
		# seems easiest way to compare
		return str(firstTree.rootTree) == str(secondTree.rootTree)

	def subTreeIndex(self, subTree, rootTree):
		return str(rootTree).find(str(subTree))

	def isFirstTreeBeforeSecondTree(self, firstIndex, secondIndex):
		return (self.subTreeIndex(firstIndex.subTree, firstTree.rootTree) < 
				self.subTreeIndex(secondIndex.subTree, rootTree.rootTree))