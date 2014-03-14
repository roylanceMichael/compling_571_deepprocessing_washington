import unittest
import nltk
import hobbs
import utils

# static variables
grammarFile = "file:../docs/grammar.cfg"
grammar = nltk.data.load(grammarFile)
parser = nltk.parse.EarleyChartParser(grammar)

class HobbsTests(unittest.TestCase):
	def test_acceptsTwoTrees(self):
		# arrange
		firstSentence = "Scientists rescued a mouse immune system."
		secondSentence = "They published the research today online."
		(firstTree, secondTree) = utils.buildTreesFromSentences(firstSentence, secondSentence, parser)

		hobbsInst = hobbs.Hobbs(firstTree, secondTree)

		# act
		pronouns = hobbsInst.findPronouns()

		# assert
		self.assertTrue(len(pronouns) == 1)
		self.assertTrue(pronouns[0] == "They")

def main():
    unittest.main()

if __name__ == '__main__':
	main()