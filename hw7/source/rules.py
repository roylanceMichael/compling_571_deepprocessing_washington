# Mike Roylance - roylance@uw.edu

class Rules:
	def __init__(self):
		self.np = "NP"
		self.s = "S"
		self.sbar = "SBAR"

		self.acceptablePronouns = {}
		self.acceptableAntecedents = {}

		# plural POS
		self.pluralPartsOfSpeech = {}
		self.singlePartsOfSpeech = {}
		self.malePartsOfSpeech = {}
		self.femalePartsOfSpeech = {}

		self.populateAcceptablePronouns()
		self.populateAcceptableAntecedents()
		self.populateNumberPartsOfSpeech()
		self.populateGenderPartsOfSpeech()

	def treeAgreement(self, pronoun, potentialAntecedent):
		if pronoun.gender != potentialAntecedent.gender:
			return "gender"

		if pronoun.number != potentialAntecedent.number:
			return "number"

		return ""

	def populateAcceptablePronouns(self):
		# hard coding the pronouns, as found in ../docs/grammar.cfg
		self.acceptablePronouns["PRP"] = None
		self.acceptablePronouns["PossPro"] = None

	def populateAcceptableAntecedents(self):
		self.acceptableAntecedents[self.s] = None
		self.acceptableAntecedents[self.sbar] = None
		self.acceptableAntecedents[self.np] = None

	def populateNumberPartsOfSpeech(self):
		self.pluralPartsOfSpeech["NNS"] = None
		self.pluralPartsOfSpeech["They"] = None
		self.pluralPartsOfSpeech["they"] = None
		self.pluralPartsOfSpeech["them"] = None
		self.singlePartsOfSpeech["NN"] = None
		self.singlePartsOfSpeech["He"] = None

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