# Mike Roylance - roylance@uw.edu
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
		parser = nltk.ChartParser(groucho_grammar)

		sent = ['I', 'shot', 'an', 'elephant', 'in', 'my', 'pajamas']

		trees = parser.nbest_parse(sent)

		self.assertTrue(len(trees) == 2)

def main():
    unittest.main()

if __name__ == '__main__':
        main()