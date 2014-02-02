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

	def test_exampleGrammarWiki(self):
		# arrange
		sent = """
(S 
	(NP she) 
	(VP 
		(VP 
			(V eats) 
			(NP 
				(Det a) 
				(N fish))) 
		(PP 
			(P with) 
			(NP (Det a) 
				(N fork)))))
		"""

		# act
		tree = nltk.Tree.parse(sent)

		# assert
		productions = tree.productions()
		
		first = productions[0]
		self.assertTrue(str(first.lhs()) == "S")
		self.assertTrue(str(first.rhs()[0]) == "NP")
		self.assertTrue(str(first.rhs()[1]) == "VP")

		second = productions[1]
		self.assertTrue(str(second.lhs()) == "NP")
		self.assertTrue(str(second.rhs()[0]) == "she")
		
		third = productions[2]
		self.assertTrue(str(third.lhs()) == "VP")
		self.assertTrue(str(third.rhs()[0]) == "VP")
		self.assertTrue(str(third.rhs()[1]) == "PP")

		fourth = productions[3]
		self.assertTrue(str(fourth.lhs()) == "VP")
		self.assertTrue(str(fourth.rhs()[0]) == "V")
		self.assertTrue(str(fourth.rhs()[1]) == "NP")

		# I think we get the picture...


def main():
    unittest.main()

if __name__ == '__main__':
        main()