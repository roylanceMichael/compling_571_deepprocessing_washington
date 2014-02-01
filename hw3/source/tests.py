# Mike Roylance - roylance@uw.edu
# Olga Whelan - olgaw@uw.edu
import unittest
import nltk

class GrammarInduce(unittest.TestCase):
	def test_getsSimpleGrammar(self):
		# arrange
		sent = "(S (NP mike) (VP walks))"

		# act
		tree = nltk.Tree.parse(sent)

		# assert
		self.assertTrue(tree.node == "S")
		pos = tree.pos()

		self.assertTrue(len(pos) == 2)

		self.assertTrue(pos[0] == ('mike', 'NP'))
		self.assertTrue(pos[1] == ('walks', 'VP'))

def main():
    unittest.main()

if __name__ == '__main__':
        main()