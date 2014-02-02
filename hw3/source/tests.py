# Mike Roylance - roylance@uw.edu
# Olga Whelan - olgaw@uw.edu
import unittest
import nltk
import induceGrammar
import cyk

class Cyk(unittest.TestCase):
	def test_buildWorkspace(self):
		# arrange
		annotatedSent = """
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

		induceInst = induceGrammar.InduceGrammar()
		induceInst.readSentence(annotatedSent)
		induceInst.createProbCfg()

		sent = ['she', 'eats', 'a', 'fish', 'with', 'a', 'fork']

		# act
		cykInst = cyk.Cyk(sent, induceInst.getProbCfg())

		# assert
		self.assertTrue(cykInst != None)

		workspace = cykInst.workspace

		self.assertTrue(workspace[0][0][0] == "NP")
		self.assertTrue(workspace[1][0][0] == "V")
		self.assertTrue(workspace[2][0][0] == "Det")
		self.assertTrue(workspace[3][0][0] == "N")
		self.assertTrue(workspace[4][0][0] == "P")
		self.assertTrue(workspace[5][0][0] == "Det")
		self.assertTrue(workspace[6][0][0] == "N")
		

class InduceGrammar(unittest.TestCase):
	def test_createCountDictionary(self):
		# arrange
		sent = "(S (NP mike) (VP walks))"
		induceInst = induceGrammar.InduceGrammar()

		# act
		induceInst.readSentence(sent)

		# assert
		grammar = induceInst.getGrammar()

		self.assertTrue(len(grammar) == 3)

		self.assertTrue(grammar["S"][("NP", "VP",)] == 1)
		self.assertTrue(grammar["NP"][("mike",)] == 1)
		self.assertTrue(grammar["VP"][("walks",)] == 1)

	def test_createProbCfg(self):
		# arrange
		sent = "(S (NP mike) (NP sun))"
		induceInst = induceGrammar.InduceGrammar()

		# act
		induceInst.readSentence(sent)
		induceInst.createProbCfg()

		# assert
		grammar = induceInst.getProbCfg()

		self.assertTrue(len(grammar) == 2)

		self.assertTrue(grammar["S"][("NP", "NP",)] == 1)
		self.assertTrue(grammar["NP"][("mike",)] == .5)
		self.assertTrue(grammar["NP"][("sun",)] == .5)

class GrammarTest(unittest.TestCase):
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