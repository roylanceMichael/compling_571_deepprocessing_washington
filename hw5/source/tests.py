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

	def test_purgeFirst(self):
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
		g.purge()

		# assert
		# this is false because see only accepts b, o | c, b | o, c
		# y is mapped to c, so see(y, x) really is checking see(c, o)
		# which isn't a valid assignment

		self.assertTrue(len(g) == 0)

	def test_purgeSecond(self):
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
		g.purge()

		# assert
		# this is false because see only accepts b, o | c, b | o, c
		# y is mapped to c, so see(y, x) really is checking see(c, o)
		# which isn't a valid assignment

		self.assertTrue(m.evaluate("see(olive, y)", g) == "Undefined")

	def test_purgeThird(self):
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
		g.purge()

		# assert
		# this works because bertie, olive are base level variables
		self.assertTrue(m.evaluate("see(bertie, olive) & boy(bertie) & -walk(bertie)", g))

	def test_quantificationFirst(self):
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
		g.purge()

		# assert
		# this checks to see if in both girl and walk there exist the same person (in this case, o)
		self.assertTrue(m.evaluate("exists x.(girl(x) & walk(x))", g))

	def test_quantificationWithoutAssignmentOfExists(self):
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
		g.purge()

		# assert
		# this checks to see if in both girl and walk there exist the same person (in this case, o)
		self.assertTrue(m.evaluate("girl(x) & walk(x)", g))

	def test_quantificationWithAssignment(self):
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
		g.purge()

		# assert
		# this checks to see if in both girl and walk there exist the same person (in this case, o)
		self.assertTrue(m.evaluate("girl(x) & walk(x)", g.add("x", "o")))

	def test_quantificationWithAssignmentFalse(self):
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
		g.purge()

		# assert
		# this checks to see if in both girl and walk there exist the same person (in this case, o)
		self.assertFalse(m.evaluate("girl(x) & walk(x)", g.add("x", "b")))

	def test_satisfiersFirst(self):
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
		lp = nltk.LogicParser()
		dom = set(['b', 'o', 'c'])
		val = nltk.parse_valuation(v)
		g = nltk.Assignment(dom, [('x', 'o'), ('y', 'c')])
		m = nltk.Model(dom, val)
		g.purge()
		fmla1 = lp.parse('girl(x) | boy(x)')

		# act
		res = m.satisfiers(fmla1, 'x', g)

		# assert
		# this checks to see if in both girl and walk there exist the same person (in this case, o)
		self.assertTrue('b' in res)
		self.assertTrue('o' in res)

	def test_satisfiersSecond(self):
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
		lp = nltk.LogicParser()
		dom = set(['b', 'o', 'c'])
		val = nltk.parse_valuation(v)
		g = nltk.Assignment(dom, [('x', 'o'), ('y', 'c')])
		m = nltk.Model(dom, val)
		g.purge()
		fmla1 = lp.parse('girl(x) -> walk(x)')

		# act
		res = m.satisfiers(fmla1, 'x', g)

		# assert
		# this is check if there is a girl who also doesn't walk
		# or not a girl who walks
		# or doesn't walk and not a girl
		self.assertTrue('c' in res)
		self.assertTrue('o' in res)
		self.assertTrue('b' in res)

	def test_satisfiersThird(self):
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
		lp = nltk.LogicParser()
		dom = set(['b', 'o', 'c'])
		val = nltk.parse_valuation(v)
		g = nltk.Assignment(dom, [('x', 'o'), ('y', 'c')])
		m = nltk.Model(dom, val)
		g.purge()
		fmla1 = lp.parse('walk(x) -> girl(x)')

		# act
		res = m.satisfiers(fmla1, 'x', g)

		# assert
		# this checks if there is someone who walks
		# but is not a girl
		# or someone who is not a girl and doesn't walk
		self.assertTrue('o' in res)
		self.assertTrue('b' in res)

	def test_satisfiersFourth(self):
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
		lp = nltk.LogicParser()
		dom = set(['b', 'o', 'c'])
		val = nltk.parse_valuation(v)
		g = nltk.Assignment(dom, [('x', 'o'), ('y', 'c')])
		m = nltk.Model(dom, val)
		g.purge()

		# act
		res = m.evaluate('all x.(girl(x) -> walk(x))', g)

		# assert
		self.assertTrue(res)

	def test_satisfiersFifth(self):
		# arrange
		v = """
bertie => b
olive => o
cyril => c
person => {b, o, c}
admire => {(b, o)}
boy => {b}
girl => {o}
dog => {c}
walk => {o, c}
see => {(b, o), (c, b), (o, c)}
"""
		lp = nltk.LogicParser()
		dom = set(['b', 'o', 'c'])
		val = nltk.parse_valuation(v)
		g = nltk.Assignment(dom, [('x', 'o'), ('y', 'c')])
		m = nltk.Model(dom, val)
		g.purge()

		# act
		res = m.evaluate('all x.(person(x) -> exists y.(person(y) & admire(x, y)))', g)

		# assert
		self.assertFalse(res)

	def test_satisfiersSixth(self):
		# arrange
		v = """
bertie => b
olive => o
cyril => c
person => {b, o, c}
admire => {(b, o)}
boy => {b}
girl => {o}
dog => {c}
walk => {o, c}
see => {(b, o), (c, b), (o, c)}
"""
		lp = nltk.LogicParser()
		dom = set(['b', 'o', 'c'])
		val = nltk.parse_valuation(v)
		g = nltk.Assignment(dom, [('x', 'o'), ('y', 'c')])
		m = nltk.Model(dom, val)
		g.purge()

		# act
		# there exists a person that admires another person
		res = m.evaluate('exists x.(person(x) -> exists y.(person(y) & admire(x, y)))', g)

		# assert
		self.assertTrue(res)

	def test_satisfiersSeventh(self):
		# arrange
		v = """
bruce => b
cyril => c
elspeth => e
julia => j
matthew => m
person => {b, e, j, m}
admire => {(j, b), (b, b), (m, e), (e, m), (c, a)}
"""
		lp = nltk.LogicParser()
		val = nltk.parse_valuation(v)
		dom = val.domain
		m = nltk.Model(dom, val)
		g = nltk.Assignment(dom)
		fmla = lp.parse("(person(x) -> exists y.(person(y) & admire(x, y)))")

		# act
		# there exists a person that admires another person
		res = m.satisfiers(fmla, 'x', g)

		# assert
		self.assertTrue("a" in res)
		self.assertTrue("j" in res)
		self.assertTrue("b" in res)
		self.assertTrue("m" in res)
		self.assertTrue("e" in res)
		self.assertTrue("c" in res)

	def test_satisfiersEigth(self):
		# arrange
		v = """
bruce => b
cyril => c
elspeth => e
julia => j
matthew => m
person => {b, e, j, m}
admire => {(j, b), (b, b), (m, e), (e, m), (c, a)}
"""
		lp = nltk.LogicParser()
		val = nltk.parse_valuation(v)
		dom = val.domain
		m = nltk.Model(dom, val)
		g = nltk.Assignment(dom)
		fmla = lp.parse("(person(y) & all x.(person(x) -> admire(x, y)))")

		# act
		# there exists a person that admires another person
		res = m.satisfiers(fmla, 'y', g)

		# assert
		self.assertTrue(len(res) == 0)

	def test_satisfiersNinth(self):
		# arrange
		v = """
bruce => b
cyril => c
elspeth => e
julia => j
matthew => m
person => {b, e, j, m}
admire => {(j, b), (b, b), (m, e), (e, m), (c, a)}
"""
		lp = nltk.LogicParser()
		val = nltk.parse_valuation(v)
		dom = val.domain
		m = nltk.Model(dom, val)
		g = nltk.Assignment(dom)
		fmla = lp.parse("(person(y) & all x.((x = bruce | x = julia) -> admire(x, y)))")

		# act
		# there exists a person that admires another person
		res = m.satisfiers(fmla, 'y', g)

		# assert
		self.assertTrue(len(res) == 1)
		self.assertTrue('b' in res)

	def test_modelBuildingFirst(self):
		# arrange
		lp = nltk.LogicParser()
		a3 = lp.parse('exists x.(man(x) & walks(x))')
		c1 = lp.parse('mortal(socrates)')
		c2 = lp.parse('-mortal(socrates)')
		mb = nltk.Mace(5)

		# act
		res1 = mb.build_model(None, [a3, c1])
		res2 = mb.build_model(None, [a3, c2])
		res3 = mb.build_model(None, [c1, c2])

		# assert
		self.assertTrue(res1)
		self.assertTrue(res2)
		self.assertFalse(res3)

	def test_modelBuildingSecond(self):
		# arrange
		lp = nltk.LogicParser()
		a = lp.parse('exists y. (woman(y) & all x. (man(x) -> love(x,y)))')
		a1 = lp.parse('man(adam)')
		a2 = lp.parse('woman(eve)')
		g = lp.parse('love(adam, eve)')
		mc = nltk.MaceCommand(g, assumptions=[a, a1, a2])

		# act
		res = mc.build_model()
		val = mc.valuation

		# assert
		self.assertTrue(res)

	def test_modelBuildingSecond(self):
		# arrange
		lp = nltk.LogicParser()
		a = lp.parse('exists y. (woman(y) & all x. (man(x) -> love(x,y)))')
		a1 = lp.parse('man(adam)')
		a2 = lp.parse('woman(eve)')
		a3 = lp.parse('all x. (man(x) -> -woman(x))')
		g = lp.parse('love(adam, eve)')
		mc = nltk.MaceCommand(g, assumptions=[a, a1, a2, a3])

		# act
		res = mc.build_model()
		val = mc.valuation

		# assert
		self.assertTrue(res)

	def test_semanticsOfEnglishFirst(self):
		# arrange
		lp = nltk.LogicParser()

		# act
		e = lp.parse(r"\x.(walk(x) & chew_gum(x))")
		
		# assert
		self.assertTrue(e != None)

	def test_semanticsOfEnglishSecond(self):
		# arrange
		lp = nltk.LogicParser()

		# act
		e = lp.parse(r"\x.(walk(x) & chew_gum(x))(gerald)")
		
		# assert
		self.assertTrue(str(e) == r"\x.(walk(x) & chew_gum(x))(gerald)")
		self.assertTrue(str(e.simplify()) == "(walk(gerald) & chew_gum(gerald))")
	
	def test_semanticsOfEnglishThird(self):
		# arrange
		lp = nltk.LogicParser()

		# act
		e = lp.parse(r'\x.\y.(dog(x) & own(y, x))(cyril)').simplify()
		e1 = lp.parse(r'\x y.(dog(x) & own(y, x))(cyril, angus)').simplify()
		
		# assert
		self.assertTrue(str(e) == r"\y.(dog(cyril) & own(y,cyril))")
		self.assertTrue(str(e1) == "(dog(cyril) & own(angus,cyril))")

	def test_semanticsOfEnglishFourth(self):
		# arrange
		lp = nltk.LogicParser()

		# act
		tvp = lp.parse(r"\X x.X(\y.chase(x,y))")
		np =  lp.parse(r'(\P.exists x.(dog(x) & P(x)))')
		#throwing an error
		# vp = nltk.sem.ApplicationExpression(tvp, np)

		# assert

	def test_semanticsOfEnglishFifth(self):
		# arrange
		parser = nltk.load_parser('simple-sem.fcfg', trace=0)
		sentence = 'Angus gives a bone to every dog'
		tokens = sentence.split()
		trees = parser.nbest_parse(tokens)

		# act
		for tree in trees:
			print tree.node['SEM']
			
		# assert


def main():
    unittest.main()

if __name__ == '__main__':
        main()