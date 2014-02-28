# Mike Roylance - roylance@uw.edu
import unittest
import nltk
import re

# In the event-style representation, there should be a one-place predicate for the type of verb event  
# (e.g. exists e. (Open(e)) ) and as many two place predicates as there are arguments of the verb 
# (e.g. Opener(e,z1) & OpenedThing(e,z2)).

def variableNormalizer(result):
	return re.sub("z[0-9]+", "{z}", result)

class PropositionLogic(unittest.TestCase):
	def test_semanticsSentences_john_eats(self):
		# arrange
		parser = nltk.load_parser('file:../docs/grammar.fcfg', trace=0)
		sentence = 'John eats'
		tokens = sentence.split()
		
		# act
		trees = parser.nbest_parse(tokens)

		# assert
		self.assertTrue(len(trees) == 1)
		expectedResult = 'exists e.(eat(e) & eater(e,john))'
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
		self.assertTrue(len(trees) == 1)
		expectedResult = 'exists x.(student(x) & exists e.(eat(e) & eater(e,x)))'
		actualResult = str(trees[0].node["SEM"])
		
		self.assertTrue(actualResult == expectedResult, actualResult)

	def test_semanticsSentences_all_student_eats(self):
		# arrange
		parser = nltk.load_parser('file:../docs/grammar.fcfg', trace=0)
		sentence = 'all students eat'
		tokens = sentence.split()
		
		# act
		trees = parser.nbest_parse(tokens)

		# assert
		self.assertTrue(len(trees) == 1)
		expectedResult = 'all x.(student(x) & exists e.(eat(e) & eater(e,x)))'
		actualResult = str(trees[0].node["SEM"])

		self.assertTrue(actualResult == expectedResult, actualResult)

	def test_semanticsSentences_john_eats_a_sandwich(self):
		# arrange
		parser = nltk.load_parser('file:../docs/grammar.fcfg', trace=0)
		sentence = 'John eats a sandwich'
		tokens = sentence.split()
		
		# act
		trees = parser.nbest_parse(tokens)

		# assert
		self.assertTrue(len(trees) == 1)
		expectedResult = 'exists e.(eat(e) & eater(e,john) & exists z.(sandwich(z) & eaten(e,john,z))))'
		actualResult = str(trees[0].node["SEM"])
		print actualResult
		self.assertTrue(actualResult == expectedResult, actualResult)

		
def main():
    unittest.main()

if __name__ == '__main__':
        main()