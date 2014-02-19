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
		tlp = nltk.LogicParser(type_check=True)

		# act
		parsed = tlp.parse('walk(angus)')

		# assert
		self.assertTrue(parsed != None, 'obviously you need to fix this')
		self.assertTrue(str(parsed.argument.type) == "e")
		self.assertTrue(str(parsed.function.type) == "<e,?>")

	def test_secondTest(self):
		# arrange
		sig = { "walk" : "<e, t>"}
		tlp = nltk.LogicParser(type_check=True)

		# act
		parsed = tlp.parse('walk(angus)', sig)

		# assert
		self.assertTrue(parsed != None, 'obviously you need to fix this')
		self.assertTrue(str(parsed.argument.type) == "e")
		self.assertTrue(str(parsed.function.type) == "<e,t>", str(parsed.function.type))

	def test_valuationFirst(self):
		# arrange
		v = """
bertie => b
olive => o
cyril => c
boy => {b}
girl => {o}
dog => {c}
walk => {o, c}
see => {(b, o), (c, b), (o, c)}
"""

		# act
		val = nltk.parse_valuation(v)

		# assert
		self.assertTrue(("b", "o") in val["see"])

def main():
    unittest.main()

if __name__ == '__main__':
        main()