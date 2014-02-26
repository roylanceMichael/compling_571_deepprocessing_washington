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

	def test_semanticsSentences_john_eats(self):
		# arrange
		parser = nltk.load_parser('file:../docs/grammar.fcfg', trace=0)
		sentence = 'John eats'
		tokens = sentence.split()
		
		# act
		trees = parser.nbest_parse(tokens)

		# assert
		# what I want...
		# eats(john)
		self.assertTrue(len(trees) == 1)
		expectedResult = 'eat(john)'
		actualResult = str(trees[0].node["SEM"])
		self.assertTrue(actualResult == expectedResult, actualResult)

	def test_semanticsSentences_a_student_eats(self):
		# arrange
		parser = nltk.load_parser('file:../docs/grammar.fcfg', trace=0)
		sentence = 'a student eats'
		tokens = sentence.split()
		
		# act
		trees = parser.nbest_parse(tokens)

		# assert
		# what I want...
		# eats(john)
		treeLen = len(trees)
		self.assertTrue(treeLen == 1)
		expectedResult = 'exists x.(student(x) & eat(x))'
		actualResult = str(trees[0].node["SEM"])
		self.assertTrue(expectedResult == actualResult, actualResult)

	def test_semanticsSentences_all_students_eat(self):
		# arrange
		parser = nltk.load_parser('file:../docs/grammar.fcfg', trace=0)
		sentence = 'all students eat'
		tokens = sentence.split()
		
		# act
		trees = parser.nbest_parse(tokens)

		# assert
		# what I want...
		# eats(john)
		self.assertTrue(len(trees) == 1)
		expectedResult = 'all x.(student(x) & eat(x))'
		actualResult = str(trees[0].node["SEM"])
		self.assertTrue(expectedResult == actualResult, actualResult)

	def test_semanticsSentences_john_eats_a_sandwich(self):
		# arrange
		parser = nltk.load_parser('file:../docs/grammar.fcfg', trace=0)
		sentence = 'John eats a sandwich'
		tokens = sentence.split()
		
		# act
		trees = parser.nbest_parse(tokens)

		# assert
		self.assertTrue(len(trees) == 1)
		expectedResult = 'exists z3.(sandwich(z3) & eat(john,z3))'
		actualResult = str(trees[0].node["SEM"])
		self.assertTrue(expectedResult == actualResult, actualResult)

	def test_semanticsSentences_all_students_eat_or_drink(self):
		# arrange
		parser = nltk.load_parser('file:../docs/grammar.fcfg', trace=0)
		sentence = 'all students eat or drink'
		# sentence = 'all students eat or drink'
		tokens = sentence.split()
		
		# act
		trees = parser.nbest_parse(tokens)

		# assert
		# self.assertTrue(len(trees) == 1)
		expectedResult = '(all x.(student(x) & eat(x)) | all x.(student(x) & drink(x)))'
		actualResult = str(trees[0].node["SEM"])
		self.assertTrue(expectedResult == actualResult, actualResult)

		
def main():
    unittest.main()

if __name__ == '__main__':
        main()