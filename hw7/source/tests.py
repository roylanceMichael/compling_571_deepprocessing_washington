import unittest
import nltk
import hobbs
import utils
import itemIndex

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
		self.assertTrue(pronouns[0].item == "They")
		self.assertTrue(pronouns[0].pos == "PRP")

	def test_acceptsAllAntecedentsWithGivenPronoun(self):
		# arrange
		firstSentence = "Scientists rescued a mouse immune system."
		secondSentence = "They published the research today online."
		(firstTree, secondTree) = utils.buildTreesFromSentences(firstSentence, secondSentence, parser)

		hobbsInst = hobbs.Hobbs(firstTree, secondTree)

		pronoun = itemIndex.ItemIndex("They", "PRP", None, None)

		# act
		antecedents = hobbsInst.comparePronounInSentences(pronoun)

		# assert
		# yes, this is working correctly right now
		self.assertTrue(len(antecedents) == 3)
		self.assertTrue(antecedents[0][1].item == "Scientists")
		self.assertTrue(antecedents[1][1].item == "Scientists")
		self.assertTrue(antecedents[2][1].item == "a")

		print antecedents[2][1].subTree
		print antecedents[2][1].subTree.leaves()
		print dir(antecedents[2][1].subTree)

def main():
    unittest.main()

if __name__ == '__main__':
	main()