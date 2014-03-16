# Mike Roylance - roylance@uw.edu

class Rules:
	def __init__(self):
		self.acceptablePronouns = {}
		self.acceptableAntecedents = {}

		# plural POS
		self.pluralPartsOfSpeech = {}
		self.malePartsOfSpeech = {}
		self.femalePartsOfSpeech = {}

		self.populateAcceptablePronouns()
		self.populateAcceptableAntecedents()
		self.populatePluralPartsOfSpeech()
		self.populateGenderPartsOfSpeech()

	def isPotentialAntecedent(self, firstIndex, secondIndex):
		if self.areTreesEqual(firstIndex, secondIndex):
			if (self.isFirstTreeBeforeSecondTree(firstIndex, secondIndex) == False and
				self.isNotPartOf(firstIndex, secondIndex)):
				return True
			return False
		return True

	def indexAgreement(self, firstIndex, secondIndex):
		if firstIndex.gender != secondIndex.gender:
			return "gender"

		if firstIndex.plurality != secondIndex.plurality:
			return "plurality"

		return ""

	def populateAcceptablePronouns(self):
		# hard coding the pronouns, as found in ../docs/grammar.cfg
		self.acceptablePronouns["PRP"] = None
		self.acceptablePronouns["PossPro"] = None

	def populateAcceptableAntecedents(self):
		self.acceptableAntecedents["S"] = None
		self.acceptableAntecedents["SBAR"] = None
		self.acceptableAntecedents["NP"] = None

	def populatePluralPartsOfSpeech(self):
		self.pluralPartsOfSpeech["NNS"] = None
		self.pluralPartsOfSpeech["They"] = None
		self.pluralPartsOfSpeech["they"] = None
		self.pluralPartsOfSpeech["them"] = None

	def populateGenderPartsOfSpeech(self):
		self.malePartsOfSpeech["researcher"] = None
		self.malePartsOfSpeech["Dr"] = None
		self.malePartsOfSpeech["Jose"] = None
		self.malePartsOfSpeech["Villadangos"] = None
		self.malePartsOfSpeech["He"] = None

		self.femalePartsOfSpeech["researcher"] = None
		self.femalePartsOfSpeech["Dr"] = None
		self.femalePartsOfSpeech["Jose"] = None
		self.femalePartsOfSpeech["Villadangos"] = None

	def areTreesEqual(self, firstIndex, secondIndex):
		# seems easiest way to compare
		return str(firstIndex.rootTree) == str(secondIndex.rootTree)

	def subTreeIndex(self, subTree, rootTree):
		return str(rootTree).find(str(subTree))

	def isFirstTreeBeforeSecondTree(self, firstIndex, secondIndex):
		firstLocation = self.subTreeIndex(firstIndex.subTree, firstIndex.rootTree)
		secondLocation = self.subTreeIndex(secondIndex.subTree, secondIndex.rootTree)
		return firstLocation < secondLocation

	def isNotPartOf(self, firstIndex, secondIndex):
		return self.subTreeIndex(firstIndex.subTree, secondIndex.subTree) == -1