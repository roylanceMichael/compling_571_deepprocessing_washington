# Mike Roylance - roylance@uw.edu
import unittest
import nltk

class PropositionLogic(unittest.TestCase):
	def test_simpleCase(self):
		# arrange
		sig = { "walk" : "<e, t>"}
		tlp = nltk.LogicParser(type_check=True)

		# act
		parsed = tlp.parse(r'\x.walk(x)(angus)', sig)

		# assert
		self.assertTrue(str(parsed.simplify()) == 'walk(angus)')

	def test_john_eats_a_sandwich(self):
		# arrange
		tlp = nltk.LogicParser()

		# john eats a sandwich
		# (\P.P(john))(\y P exists e.(eat(e) & eater(e,y) & P(x)))
		# act
		# parsed = tlp.parse(r'(\P.P(john))(\x.see(y,x))')
		# 
		parsed = tlp.parse(r'(\P.P(john))(\y exists e.(eat(e) & eater(e,y) & (\P.P(john))(\r.exists x.(sandwich(x) & eaten(e,r,x)))))')

		# assert
		#print str(parsed.simplify())

	def test_john_eats_a_sandwich1(self):
		# arrange
		tlp = nltk.LogicParser()
		np = r'(\P.P(john))'
		vp = r'(\x\Q.exists e.(eat(e) & eater(e,x) & Q(x)))'
		det = r'(\P Q.exists x.(P(x) & eaten(x)))'
		np2 = r'(\x.sandwich(x))'

		print str((tlp.parse(np + vp)).simplify())
		print str((tlp.parse(det + np2)).simplify())

		print str((tlp.parse(np + vp + det + np2)).simplify())

		# assert

def main():
    unittest.main()

if __name__ == '__main__':
        main()