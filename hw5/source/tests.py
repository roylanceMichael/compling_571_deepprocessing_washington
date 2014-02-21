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

	def test_valuationSecond(self):
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
		dom = set(['b', 'o', 'c'])
		val = nltk.parse_valuation(v)

		# act
		g = nltk.Assignment(dom, [('x', 'o'), ('y', 'c')])
		m = nltk.Model(dom, val)

		# assert
		# this is because "see" has a set of (o, c) - where c could be y in this case
		self.assertTrue(m.evaluate('see(olive, y)', g))

	def test_valuationThird(self):
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
		dom = set(['b', 'o', 'c'])
		val = nltk.parse_valuation(v)

		# act
		g = nltk.Assignment(dom, [('x', 'o'), ('y', 'c')])
		m = nltk.Model(dom, val)

		# assert
		# this is because in dom we assigned b, o and c
		# and in the assignment, we mapped 'x' to 'o' and 'y' to 'c'
		# therefore, 'y' gets mapped back to 'c'
		self.assertTrue(g['y'] == 'c')

	def test_valuationFourth(self):
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
		dom = set(['b', 'o', 'c'])
		val = nltk.parse_valuation(v)

		# act
		g = nltk.Assignment(dom, [('x', 'o'), ('y', 'c')])
		m = nltk.Model(dom, val)

		# assert
		# this is false because see only accepts b, o | c, b | o, c
		# y is mapped to c, so see(y, x) really is checking see(c, o)
		# which isn't a valid assignment
		self.assertFalse(m.evaluate('see(y, x)', g))

def main():
    unittest.main()

if __name__ == '__main__':
        main()