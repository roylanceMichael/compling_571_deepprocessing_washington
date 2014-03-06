# Mike Roylance - roylance@uw.edu
import unittest
import nltk
from nltk.corpus import wordnet as wn
import resnik

class WordNetInterface(unittest.TestCase):
	def test_first(self):
		# arrange
		# act
		res = wn.synsets('dog')

		# assert
		self.assertTrue(len(res) == 8)

	def test_second(self):
		# arrange
		# act
		res = wn.synset('dog.n.01')
		examples = res.examples
		lemmas = res.lemmas

		# assert
		self.assertTrue(res.definition == 'a member of the genus Canis (probably descended from the common wolf) that has been domesticated by man since prehistoric times; occurs in many breeds')
		
		self.assertTrue(len(examples) == 1)
		self.assertTrue(examples[0] == 'the dog barked all night')
		self.assertTrue(len(lemmas) == 3)

class Reznik(unittest.TestCase):
	def test_simple(self):
		# arrange
		ic = nltk.corpus.wordnet_ic.ic('ic-brown-resnik-add1.dat')
		resnikInstance = resnik.Resnik(ic)

		# act
		items = list(resnikInstance.processLine("tie	jacket,suit"))

		# assert
		self.assertTrue(len(items) == 4)

def main():
    unittest.main()

if __name__ == '__main__':
	main()