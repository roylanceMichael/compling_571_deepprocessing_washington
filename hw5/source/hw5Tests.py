# Mike Roylance - roylance@uw.edu
import unittest
import nltk
import re

def variableNormalizer(result):
	return re.sub("z[0-9]+", "{z}", result)

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
		expectedResult = 'all {z}.(dog({z}) -> exists {z}.(bone({z}) & give(angus,{z},{z})))'
		
		#print expectedResult
		#print trees[0].node["SEM"]
		self.assertTrue(expectedResult == variableNormalizer(str(trees[0].node["SEM"])))

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
		expectedResult = 'eater(john)'
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
		expectedResult = 'exists x.(student(x) & eater(x))'
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
		expectedResult = 'all x.(student(x) & eater(x))'
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
		expectedResult = 'exists {z}.(sandwich({z}) & eat(john,{z}))'
		actualResult = variableNormalizer(str(trees[0].node["SEM"]))
		self.assertTrue(expectedResult == actualResult, actualResult)

	def test_semanticsSentences_all_students_eat_or_drink(self):
		# arrange
		parser = nltk.load_parser('file:../docs/grammar.fcfg', trace=0)
		sentence = 'all students eat or drink'
		tokens = sentence.split()
		
		# act
		trees = parser.nbest_parse(tokens)

		# assert
		expectedResult = '(all x.(student(x) & eater(x)) | all x.(student(x) & drinker(x)))'
		actualResult = str(trees[0].node["SEM"])
		self.assertTrue(expectedResult == actualResult, actualResult)

	def test_semanticsSentences_john_drinks_a_soda_or_eats_a_sandwich(self):
		# arrange
		parser = nltk.load_parser('file:../docs/grammar.fcfg', trace=0)
		sentence = 'John drinks a soda or eats a sandwich'
		tokens = sentence.split()
		
		# act
		trees = parser.nbest_parse(tokens)

		# assert
		expectedResult = '(exists {z}.(soda({z}) & drink(john,{z})) | exists {z}.(sandwich({z}) & eat(john,{z})))'
		actualResult = variableNormalizer(str(trees[0].node["SEM"]))

		self.assertTrue(expectedResult == actualResult, actualResult)

	def test_semanticsSentences_john_or_mary_eats(self):
		# arrange
		parser = nltk.load_parser('file:../docs/grammar.fcfg', trace=0)
		sentence = 'John or Mary eats'

		tokens = sentence.split()
		
		# act
		trees = parser.nbest_parse(tokens)

		# assert
		expectedResult = '(eater(john) | eater(mary))'
		actualResult = variableNormalizer(str(trees[0].node["SEM"]))
		self.assertTrue(expectedResult == actualResult, actualResult)

	def test_semanticsSentences_a_student_writes_an_essay_or_eats(self):
		# arrange
		parser = nltk.load_parser('file:../docs/grammar.fcfg', trace=0)
		sentence = 'a student writes an essay or eats'

		tokens = sentence.split()
		
		# act
		trees = parser.nbest_parse(tokens)

		# assert
		expectedResult = '(exists x.(student(x) & exists {z}.(essay({z}) & write(x,{z}))) | exists x.(student(x) & eater(x)))'
		actualResult = variableNormalizer(str(trees[0].node["SEM"]))
		
		self.assertTrue(expectedResult == actualResult, actualResult)

	def test_semanticsSentences_every_student_eats_a_sandwich_or_drinks_a_soda(self):
		# arrange
		parser = nltk.load_parser('file:../docs/grammar.fcfg', trace=0)
		sentence = 'every student eats a sandwich or drinks a soda'

		tokens = sentence.split()
		
		# act
		trees = parser.nbest_parse(tokens)

		# assert
		expectedResult = '(all x.(student(x) & exists {z}.(sandwich({z}) & eat(x,{z}))) | all x.(student(x) & exists {z}.(soda({z}) & drink(x,{z}))))'
		actualResult = variableNormalizer(str(trees[0].node["SEM"]))
		
		self.assertTrue(expectedResult == actualResult, actualResult)

	def test_semanticsSentences_john_eats_every_sandwich(self):
		# arrange
		parser = nltk.load_parser('file:../docs/grammar.fcfg', trace=0)
		sentence = 'John eats every sandwich'

		tokens = sentence.split()
		
		# act
		trees = parser.nbest_parse(tokens)

		# assert
		expectedResult = 'all {z}.(sandwich({z}) & eat(john,{z}))'
		actualResult = variableNormalizer(str(trees[0].node["SEM"]))
		
		self.assertTrue(expectedResult == actualResult, actualResult)

	def test_semanticsSentences_john_eats_every_sandwich_or_bagel(self):
		# arrange
		parser = nltk.load_parser('file:../docs/grammar.fcfg', trace=0)
		sentence = 'John eats every sandwich or bagel'

		tokens = sentence.split()
		
		# act
		trees = parser.nbest_parse(tokens)

		# assert
		expectedResult = '(all {z}.(sandwich({z}) & eat(john,{z})) | all {z}.(bagel({z}) & eat(john,{z})))'
		actualResult = variableNormalizer(str(trees[0].node["SEM"]))
		
		self.assertTrue(expectedResult == actualResult, actualResult)

	def test_semanticsSentences_nobody_eats_a_bagel(self):
		# arrange
		parser = nltk.load_parser('file:../docs/grammar.fcfg', trace=0)
		sentence = 'nobody eats a bagel'

		tokens = sentence.split()
		
		# act
		trees = parser.nbest_parse(tokens)

		# assert
		expectedResult = '-all x.(person(x) & exists {z}.(bagel({z}) & eat(x,{z})))'
		actualResult = variableNormalizer(str(trees[0].node["SEM"]))
		
		self.assertTrue(expectedResult == actualResult, actualResult)

	def test_semanticsSentences_a_person_does_not_eat(self):
		# arrange
		parser = nltk.load_parser('file:../docs/grammar.fcfg', trace=0)
		sentence = 'a person does not eat'

		tokens = sentence.split()
		
		# act
		trees = parser.nbest_parse(tokens)

		# assert
		expectedResult = 'exists x.(person(x) & -eater(x))'
		actualResult = variableNormalizer(str(trees[0].node["SEM"]))

		self.assertTrue(expectedResult == actualResult, actualResult)

	def test_semanticsSentences_jack_does_not_eat_or_drink(self):
		# arrange
		parser = nltk.load_parser('file:../docs/grammar.fcfg', trace=0)
		sentence = 'Jack does not eat or drink'

		tokens = sentence.split()
		
		# act
		trees = parser.nbest_parse(tokens)

		# assert
		expectedResult = '(-eater(jack) & -drinker(jack))'
		actualResult = variableNormalizer(str(trees[0].node["SEM"]))
		
		self.assertTrue(expectedResult == actualResult, actualResult)

	def test_semanticsSentences_no_student_eats_a_bagel(self):
		# arrange
		parser = nltk.load_parser('file:../docs/grammar.fcfg', trace=0)
		sentence = 'no student eats a bagel'

		tokens = sentence.split()
		
		# act
		trees = parser.nbest_parse(tokens)

		# assert
		expectedResult = '-all x.(student(x) & exists {z}.(bagel({z}) & eat(x,{z})))'
		actualResult = variableNormalizer(str(trees[0].node["SEM"]))

		self.assertTrue(expectedResult == actualResult, actualResult)

	def test_semanticsSentences_john_eats_in_seattle(self):
		# arrange
		parser = nltk.load_parser('file:../docs/grammar.fcfg', trace=0)
		sentence = 'John eats in Seattle'

		tokens = sentence.split()
		
		# act
		trees = parser.nbest_parse(tokens)

		# assert
		expectedResult = '(eater(john) & in(john,seattle))'
		actualResult = variableNormalizer(str(trees[0].node["SEM"]))

		self.assertTrue(expectedResult == actualResult, actualResult)

		
def main():
    unittest.main()

if __name__ == '__main__':
        main()