import unittest
import nltk

class GrammarTests(unittest.TestCase):
	def test_basicGrammarExample(self):
		groucho_grammar = nltk.parse_cfg("""
S -> NP VP
PP -> P NP
NP -> Det N | Det N PP | 'I'
VP -> V NP | VP PP
Det -> 'an' | 'my'
N -> 'elephant' | 'pajamas'
V -> 'shot'
P -> 'in'
""")

		sent = ['I', 'shot', 'an', 'elephant', 'in', 'my', 'pajamas']

		parser = nltk.ChartParser(groucho_grammar)

		trees = parser.nbest_parse(sent)

		self.assertTrue(len(trees) == 2)

	def test_loadToyGrammar(self):
		grammar = nltk.data.load("file:../testDocs/toy.cfg")

		parser = nltk.parse.EarleyChartParser(grammar)

		sent = ['the', 'dog', 'sat']

		trees = parser.nbest_parse(sent)

		self.assertTrue(grammar != None)

	def test_firstSentence(self):
		grammar = nltk.data.load("file:../testDocs/grammar.cfg")

		parser = nltk.parse.EarleyChartParser(grammar)

		sent = ['scientists', 'rescued', 'a', 'mouse', 'immune', 'system']

		trees = parser.nbest_parse(sent)

		self.assertTrue(len(trees) > 0)

	def test_secondSentence(self):
		grammar = nltk.data.load("file:../testDocs/grammar.cfg")

		parser = nltk.parse.EarleyChartParser(grammar)

		sent = ['will', 'this', 'work', 'in', 'humans', '?']

		trees = parser.nbest_parse(sent)

		self.assertTrue(len(trees) > 0)

	def test_thirdSentence(self):
		grammar = nltk.data.load("file:../testDocs/grammar.cfg")

		parser = nltk.parse.EarleyChartParser(grammar)

		# They published their research today online.
		sent = nltk.word_tokenize('they published their research today online.')

		trees = parser.nbest_parse(sent)

		self.assertTrue(len(trees) > 0)

	def test_fourthSentence(self):
		grammar = nltk.data.load("file:../testDocs/grammar.cfg")

		parser = nltk.parse.EarleyChartParser(grammar)

		# They published their research today online.
		sent = nltk.word_tokenize('the immune response is alerted by dendritic cells.')

		trees = parser.nbest_parse(sent)

		self.assertTrue(len(trees) > 0)

	def test_fifthSentence(self):
		grammar = nltk.data.load("file:../testDocs/grammar.cfg")

		parser = nltk.parse.EarleyChartParser(grammar)

		# They published their research today online.
		sent = nltk.word_tokenize('they capture infected cells and display fragments of the pathogen.')

		trees = parser.nbest_parse(sent)

		self.assertTrue(len(trees) > 0)

	def test_sixthSentence(self):
		grammar = nltk.data.load("file:../testDocs/grammar.cfg")

		parser = nltk.parse.EarleyChartParser(grammar)

		# They published their research today online.
		sent = nltk.word_tokenize('dr Jose Villadangos is a researcher of the immune system.')

		trees = parser.nbest_parse(sent)

		self.assertTrue(len(trees) > 0)

	def test_seventhSentence(self):
		grammar = nltk.data.load("file:../testDocs/grammar.cfg")

		parser = nltk.parse.EarleyChartParser(grammar)

		# They published their research today online.
		sent = nltk.word_tokenize('dr Jose Villadangos is a researcher of the immune system.')

		trees = parser.nbest_parse(sent)

		self.assertTrue(len(trees) > 0)

def main():
    unittest.main()

if __name__ == '__main__':
        main()