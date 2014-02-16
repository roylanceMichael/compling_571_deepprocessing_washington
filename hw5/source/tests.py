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

	def test_valuationMapping(self):
		# arrange
		p = ('P', True)
		q = ('Q', True)
		r = ('R', False)

		# act
		val = nltk.Valuation([p, q, r])

		# assert
		self.assertTrue(val['P'])
		self.assertTrue(val['Q'])
		self.assertFalse(val['R'])

	def test_model(self):
		# arrange
		p = ('P', True)
		q = ('Q', True)
		r = ('R', False)
		val = nltk.Valuation([p, q, r])
		dom = set([])
		g = nltk.Assignment(dom)

		# act
		m = nltk.Model(dom, val)

		# assert
		self.assertTrue(m.evaluate('(P & Q)', g))
		self.assertFalse(m.evaluate('-(P & Q)', g))
		self.assertFalse(m.evaluate('(P & R)', g))
		self.assertTrue(m.evaluate('(P | R)', g))

class FirstOrderLogic(unittest.TestCase):
	def test_firstTest(self):
		# arrange
		# act
		# assert
		self.assertTrue(False, 'obviously you need to fix this')

def main():
    unittest.main()

if __name__ == '__main__':
        main()