class Rules:
	def __init__(self):
		self.acceptablePronouns = {}
		self.acceptableAntecedents = {}

		self.populateAcceptablePronouns()
		self.populateAcceptableAntecedents()

	def populateAcceptablePronouns(self):
		# hard coding the pronouns, as found in ../docs/grammar.cfg
		self.acceptablePronouns["PRP"] = None
		self.acceptablePronouns["PossPro"] = None

	def populateAcceptableAntecedents(self):
		self.acceptableAntecedents["S"] = None
		self.acceptableAntecedents["NP"] = None