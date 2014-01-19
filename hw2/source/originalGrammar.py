import nltk

class OriginalGrammar:
	def __init__(self, contextFreeGrammar):
		self.contextFreeGrammar = contextFreeGrammar
		self.productions = nltk.parse_cfg(contextFreeGrammar)

	