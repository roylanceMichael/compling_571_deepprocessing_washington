# Mike Roylance - roylance@uw.edu
import unittest
import nltk

class PropositionLogic(unittest.TestCase):
	def test_verifyBeingNorthIsAnAssymetricalStatement(self):
		# arrange
		lp = nltk.LogicParser()
		SnF = lp.parse('SnF')
		NotFns = lp.parse('-FnS')
		R = lp.parse('SnF -> -FnS')
		prover = nltk.Prover9()

		# act
		result = prover.prove(NotFns, [SnF, R])

		# assert
		self.assertTrue(result)

def main():
    unittest.main()

if __name__ == '__main__':
        main()