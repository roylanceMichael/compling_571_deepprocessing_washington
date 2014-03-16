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
		travTree = traversableTree.TraversableTree(firstTree, None)

		# assert
		self.assertTrue(travTree != None)

		self.assertTrue(len(travTree.children) == 3)
		np = travTree.children[0]

		self.assertTrue(np.parent == travTree.tree)


def main():
    unittest.main()

if __name__ == '__main__':
	main()