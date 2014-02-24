# Mike Roylance - roylance@uw.edu
import unittest
import nltk


class PropositionLogic(unittest.TestCase):
	def test_semanticsOfEnglishFirst(self):
		# arrange
		parser = nltk.load_parser('file:../docs/simple-sem.fcfg', trace=0)
		sentence = 'Angus gives a bone to every dog'
		tokens = sentence.split()
		
		# act
		trees = parser.nbest_parse(tokens)

		# assert
		self.assertTrue(len(trees) == 1)
		expectedResult = 'all z2.(dog(z2) -> exists z1.(bone(z1) & give(angus,z1,z2)))'
		
		#print expectedResult
		#print trees[0].node["SEM"]
		self.assertTrue(expectedResult == str(trees[0].node["SEM"]))
		
def main():
    unittest.main()

if __name__ == '__main__':
        main()