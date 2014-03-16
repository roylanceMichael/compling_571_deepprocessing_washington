import unittest
import nltk
import hobbs
import utils
import itemIndex
import rules

# static variables
grammarFile = "file:../docs/grammar.cfg"
grammar = nltk.data.load(grammarFile)
parser = nltk.parse.EarleyChartParser(grammar)
rules = rules.Rules()

class HobbsTests(unittest.TestCase):
	def test_acceptsTwoTrees(self):
		# arrange
		firstSentence = "Scientists rescued a mouse immune system."
		secondSentence = "They published the research today online."
		(firstTree, secondTree) = utils.buildTreesFromSentences(firstSentence, secondSentence, parser)

		hobbsInst = hobbs.Hobbs(firstTree, secondTree)

		# act
		pronouns = list(hobbsInst.findPronouns())

		# assert
		self.assertTrue(len(pronouns) == 1)
		self.assertTrue(str(pronouns[0].items[0].rhs()[0]) == "They", pronouns[0].items[0].rhs()[0])
		self.assertTrue(pronouns[0].pos == "PRP")

	def test_acceptsAllAntecedentsWithGivenPronoun(self):
		# arrange
		firstSentence = "Scientists rescued a mouse immune system."
		secondSentence = "They published the research today online."
		(firstTree, secondTree) = utils.buildTreesFromSentences(firstSentence, secondSentence, parser)

		hobbsInst = hobbs.Hobbs(firstTree, secondTree)

		pronoun = list(hobbsInst.findPronouns())[0]

		# act
		antecedents = list(hobbsInst.comparePronounInTree(pronoun, hobbsInst.firstTree))

		# assert
		# yes, this is working correctly right now
		self.assertTrue(len(antecedents) == 3, str(len(antecedents)))
		self.assertTrue(str(antecedents[0].items[0].rhs()[0]) == "Scientists")
		self.assertTrue(str(antecedents[1].items[0].rhs()[0]) == "Scientists")

	def test_acceptsAllAntecedentsWithGivenPronounForSecondSentence(self):
		# arrange
		firstSentence = "Scientists rescued a mouse immune system."
		secondSentence = "They published the research today online."
		(firstTree, secondTree) = utils.buildTreesFromSentences(firstSentence, secondSentence, parser)

		hobbsInst = hobbs.Hobbs(firstTree, secondTree)

		pronoun = list(hobbsInst.findPronouns())[0]

		# act
		antecedents = list(hobbsInst.comparePronounInSentences(pronoun))

		# assert
		# yes, this is working correctly right now
		self.assertTrue(len(antecedents) == 3, str(len(antecedents)))
		
		self.assertTrue(str(antecedents[0].items[0].rhs()[0]) == "Scientists", antecedents[0].items[0])
		self.assertTrue(str(antecedents[1].items[0].rhs()[0]) == "Scientists", antecedents[1].items[0])

class RulesTests(unittest.TestCase):
	def test_handlesGenderAndPluralityCorrectly_they(self):
		# arrange
		firstSentence = "Scientists rescued a mouse immune system."
		secondSentence = "They published the research today online."
		(firstTree, secondTree) = utils.buildTreesFromSentences(firstSentence, secondSentence, parser)

		hobbsInst = hobbs.Hobbs(firstTree, secondTree)

		# act
		pronoun = list(hobbsInst.findPronouns())[0]

		# assert
		self.assertTrue(pronoun.gender == "u")
		self.assertTrue(pronoun.plurality == "pl", pronoun.plurality)

	def test_handlesGenderAndPluralityCorrectly_he(self):
		# arrange
		firstSentence = "Scientists rescued a mouse immune system."
		secondSentence = "He published the research today online."
		(firstTree, secondTree) = utils.buildTreesFromSentences(firstSentence, secondSentence, parser)

		hobbsInst = hobbs.Hobbs(firstTree, secondTree)

		# act
		pronoun = list(hobbsInst.findPronouns())[0]

		# assert
		self.assertTrue(pronoun.gender == "m")
		self.assertTrue(pronoun.plurality == "sg")

def main():
    unittest.main()

if __name__ == '__main__':
	main()