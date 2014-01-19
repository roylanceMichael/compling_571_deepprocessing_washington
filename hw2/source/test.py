# Mike Roylance - roylance@uw.edu
import unittest
import nltk
import originalGrammar

class OriginalGrammar(unittest.TestCase):
	def test_createsBasicGrammarStructure(self):
		# arrange
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
		# act
		origGrammar = originalGrammar.OriginalGrammar(testGrammar)

		# assert
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

	def test_addsUniqueStartState(self):
		# arrange
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
		# act
		origGrammar = originalGrammar.OriginalGrammar(testGrammar)
		origGrammar.convertFirstStep()

		# assert
		self.assertTrue(origGrammar.cnfProductions[0] != None)
		self.assertTrue(origGrammar.cnfProductions[0].getLhs() != None)

	def test_findStartNode(self):
		# arrange
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
		# act
		origGrammar = originalGrammar.OriginalGrammar(testGrammar)
		startNode = origGrammar.findStartNode()

		# assert
		print startNode
		self.assertTrue(startNode == "S", startNode)
		

def main():
    unittest.main()

if __name__ == '__main__':
        main()