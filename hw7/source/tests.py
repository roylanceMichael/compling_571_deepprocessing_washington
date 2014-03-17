# Mike Roylance - roylance@uw.edu

import unittest
import nltk
import hobbs
import utils
import itemIndex
import rules
import traversableTree

# static variables
grammarFile = "file:../docs/grammar.cfg"
grammar = nltk.data.load(grammarFile)
parser = nltk.parse.EarleyChartParser(grammar)
rules = rules.Rules()

class TraversableTreeTests(unittest.TestCase):
	def test_creates_traversing_tree(self):
		# arrange
		firstSentence = "Scientists rescued a mouse immune system."
		secondSentence = "They published the research today online."
		(firstTree, secondTree) = utils.buildTreesFromSentences(firstSentence, secondSentence, parser)

		# act
		travTree = traversableTree.TraversableTree(firstTree, None, rules)

		# assert
		self.assertTrue(travTree != None)

		self.assertTrue(len(travTree.children) == 3)
		np = travTree.children[0]

		self.assertTrue(np.parent == travTree)

class HobbsTests(unittest.TestCase):
	def test_ctor_finds_pronouns(self):
		# arrange
		firstSentence = "Scientists rescued a mouse immune system."
		secondSentence = "They published the research today online."
		(firstTree, secondTree) = utils.buildTreesFromSentences(firstSentence, secondSentence, parser)

		# act
		hobbsInst = hobbs.Hobbs(firstTree, secondTree)

		# assert
		self.assertTrue(len(hobbsInst.foundPronouns) == 1, str(len(hobbsInst.foundPronouns)))

	def test_determines_antecedents(self):
		# arrange
		firstSentence = "Scientists rescued a mouse immune system."
		secondSentence = "They published the research today online."
		(firstTree, secondTree) = utils.buildTreesFromSentences(firstSentence, secondSentence, parser)
		hobbsInst = hobbs.Hobbs(firstTree, secondTree)

		# act
		results = list(hobbsInst.findAntecedents())

		# assert
		self.assertTrue(len(hobbsInst.foundPronouns) == 1, str(len(hobbsInst.foundPronouns)))
		self.assertTrue(len(results) == 7, str(len(results)))

	def test_determines_antecedents_difficult(self):
		# arrange
		firstSentence = "Scientists restored immunity in mice with a weak immune system."
		secondSentence = "They injected them with a live vaccine."
		(firstTree, secondTree) = utils.buildTreesFromSentences(firstSentence, secondSentence, parser)
		hobbsInst = hobbs.Hobbs(firstTree, secondTree)

		# act
		results = list(hobbsInst.findAntecedents())

		# assert
		self.assertTrue(len(hobbsInst.foundPronouns) == 2, str(len(hobbsInst.foundPronouns)))
		self.assertTrue(len(results) == 24, str(len(results)))


def main():
    unittest.main()

if __name__ == '__main__':
	main()