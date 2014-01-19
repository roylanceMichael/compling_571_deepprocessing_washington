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
		self.assertTrue(self.getSymbolFromProduction(origGrammar, 0, True) == 'S')
		
		firstRhs = self.getSymbolFromProduction(origGrammar, 0, False)
		self.assertTrue(str(firstRhs[0]) == 'A')
		self.assertTrue(str(firstRhs[1]) == 'S')
		self.assertTrue(str(firstRhs[2]) == 'B')

		# second production
		self.assertTrue(self.getSymbolFromProduction(origGrammar, 1, True) == 'A')

		secondRhs = self.getSymbolFromProduction(origGrammar, 1, False)
		self.assertTrue(str(secondRhs[0]) == 'a')
		self.assertTrue(str(secondRhs[1]) == 'A')
		self.assertTrue(str(secondRhs[2]) == 'S')

		# third production
		thirdProduction = origGrammar.getProduction(2)
		self.assertTrue(thirdProduction['lhs'] == 'A')
		self.assertTrue(len(thirdProduction['rhs']) == 1)
		self.assertTrue(thirdProduction['rhs'][0] == 'a')

		# fourth production
		fourthProduction = origGrammar.getProduction(3)
		self.assertTrue(fourthProduction['lhs'] == 'A')
		self.assertTrue(len(fourthProduction['rhs']) == 0)

		# fifth production
		fifthProduction = origGrammar.getProduction(4)
		self.assertTrue(fifthProduction['lhs'] == 'B')
		self.assertTrue(len(fifthProduction['rhs']) == 3)
		self.assertTrue(fifthProduction['rhs'][0] == 'S')
		self.assertTrue(fifthProduction['rhs'][1] == 'b')
		self.assertTrue(fifthProduction['rhs'][2] == 'S')

		# sixth production
		sixthProduction = origGrammar.getProduction(5)
		self.assertTrue(sixthProduction['lhs'] == 'B')
		self.assertTrue(len(sixthProduction['rhs']) == 1)
		self.assertTrue(sixthProduction['rhs'][0] == 'A')

		# seventh production
		seventhProduction = origGrammar.getProduction(6)
		self.assertTrue(seventhProduction['lhs'] == 'B')
		self.assertTrue(len(seventhProduction['rhs']) == 2)
		self.assertTrue(seventhProduction['rhs'][0] == 'b')
		self.assertTrue(seventhProduction['rhs'][1] == 'b')

		# eigth production
		eigthProduction = origGrammar.getProduction(7)
		self.assertTrue(eigthProduction['lhs'] == 'a')
		self.assertTrue(len(eigthProduction['rhs']) == 1)
		self.assertTrue(eigthProduction['rhs'][0] == 'a')

		# ninth production
		ninthProduction = origGrammar.getProduction(8)
		self.assertTrue(ninthProduction['lhs'] == 'b')
		self.assertTrue(len(ninthProduction['rhs']) == 1)
		self.assertTrue(ninthProduction['rhs'][0] == 'b')

def main():
    unittest.main()

if __name__ == '__main__':
        main()