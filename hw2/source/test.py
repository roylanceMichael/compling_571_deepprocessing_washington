# Mike Roylance - roylance@uw.edu
import unittest
import nltk
import originalGrammar

class GrammarTests(unittest.TestCase):
	def getSymbolFromProduction(self, grammars, idx, leftSide):
		if leftSide:
			return grammars.productions[idx].lhs().symbol()
		return grammars.productions[idx].rhs()

	def test_basicGrammarExample(self):
		testGrammar = """
S -> A S B

A -> a A S
A -> a
A -> 

B -> S b S
B -> A
B -> b b

a -> 'a'
b -> 'b'
"""
		origGrammar = originalGrammar.OriginalGrammar(testGrammar)

		self.assertTrue(len(origGrammar.productions) > 8)
		
		# first production
		self.assertTrue(origGrammar.productions[0].getLhs() == 'S')
		
		firstRhs = origGrammar.productions[0].getRhs()
		self.assertTrue(str(firstRhs[0]) == 'A')
		self.assertTrue(str(firstRhs[1]) == 'S')
		self.assertTrue(str(firstRhs[2]) == 'B')

		# second production
		self.assertTrue(origGrammar.productions[1].getLhs() == 'A')

		secondRhs = origGrammar.productions[1].getRhs()
		self.assertTrue(str(secondRhs[0]) == 'a')
		self.assertTrue(str(secondRhs[1]) == 'A')
		self.assertTrue(str(secondRhs[2]) == 'S')

		# third production
		self.assertTrue(origGrammar.productions[2].getLhs() == 'A')
		thirdRhs = origGrammar.productions[2].getRhs()
		self.assertTrue(len(thirdRhs) == 1)
		self.assertTrue(thirdRhs[0] == 'a')

def main():
    unittest.main()

if __name__ == '__main__':
        main()