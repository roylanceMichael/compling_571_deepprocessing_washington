# Mike Roylance - roylance@uw.edu
import unittest
import nltk
import originalGrammar
import cfgTransform

class CfgTransform(unittest.TestCase):
	def test_createsNonTerminalDictionary(self):
		# arrange
		testGrammar = """
R -> 'a' 'b' 'c'
"""
		transform = cfgTransform.CfgTransform(testGrammar)

		# act
		transform.buildCnf()

		# assert
		self.assertTrue(len(transform.terminalToNonTerminal) == 3)
		self.assertTrue(transform.terminalToNonTerminal['a'] == 'R')
		self.assertTrue(transform.terminalToNonTerminal['b'] == 'R1')
		self.assertTrue(transform.terminalToNonTerminal['c'] == 'R2')

	def test_createsNonTerminalDictionaryFromHigherLevel(self):
		# arrange
		testGrammar = """
S -> R
R -> 'a' 'b' 'c'
"""
		transform = cfgTransform.CfgTransform(testGrammar)

		# act
		transform.buildCnf()

		# assert
		self.assertTrue(len(transform.terminalToNonTerminal) == 3)
		self.assertTrue(transform.terminalToNonTerminal['a'] == 'R')
		self.assertTrue(transform.terminalToNonTerminal['b'] == 'R1')
		self.assertTrue(transform.terminalToNonTerminal['c'] == 'R2')

def main():
    unittest.main()

if __name__ == '__main__':
        main()