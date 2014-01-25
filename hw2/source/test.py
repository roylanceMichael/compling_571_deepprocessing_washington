# Mike Roylance - roylance@uw.edu
import unittest
import nltk
import cfgToCnfBuilder
import productionBuilder

class ProductionBuilder(unittest.TestCase):
	def test_buildsNewProductionWithoutLhs(self):
		# arrange
		pb = productionBuilder.ProductionBuilder()

		rhs = tuple([nltk.Nonterminal('F')])

		# act
		prod = pb.build(rhs)

		# assert
		lhs = prod.lhs()
		rhs = prod.rhs()

		self.assertTrue(str(lhs) == 'X1')
		self.assertTrue(str(rhs[0]) == 'F')

class CfgToCnfBuilder(unittest.TestCase):
	def test_terminalIsInCnf(self):
		# arrange
		testGrammar = """
R -> 'a'
"""
		builder = cfgToCnfBuilder.CfgToCnfBuilder(testGrammar)

		# act
		builder.build()

		# assert
		cnfProductions = builder.getFinalProductions()
		self.assertTrue(len(cnfProductions) == 1)

		rhs = cnfProductions[0].rhs()

		self.assertTrue(str(rhs[0]) == 'a')

	def test_nonTerminalsAreInCnf(self):
		# arrange
		testGrammar = """
R -> C F
"""
		builder = cfgToCnfBuilder.CfgToCnfBuilder(testGrammar)

		# act
		builder.build()

		# assert
		cnfProductions = builder.getFinalProductions()
		
		self.assertTrue(len(cnfProductions) == 1)

		rhs = cnfProductions[0].rhs()
		self.assertTrue(str(rhs[0]) == 'C')
		self.assertTrue(str(rhs[1]) == 'F')

	def test_moreThanOneTerminalCreatesNewNonTerminals(self):
		# arrange
		testGrammar = """
R -> 'a' 'b'
"""
		
		# expecting 
		# R -> R1 R2
		# R1 -> 'a'
		# R2 -> 'b'

		builder = cfgToCnfBuilder.CfgToCnfBuilder(testGrammar)

		# act
		builder.build()

		# assert
		cnfProductions = builder.getFinalProductions()
		
		self.assertTrue(len(cnfProductions) == 3)

		rhs1 = cnfProductions[0].rhs()
		rhs2 = cnfProductions[1].rhs()
		rhs3 = cnfProductions[2].rhs()
		self.assertTrue(str(rhs1[0]) == 'X1')
		self.assertTrue(str(rhs1[1]) == 'X2')
		self.assertTrue(str(rhs2[0]) == 'a')
		self.assertTrue(str(rhs3[0]) == 'b')

	def test_threeNonTerminals(self):
		# arrange
		testGrammar = """
R -> A B C
"""
		
		# expecting 
		# R -> X1 C
		# X1 -> A B 

		builder = cfgToCnfBuilder.CfgToCnfBuilder(testGrammar)

		# act
		builder.build()

		# assert
		cnfProductions = builder.getFinalProductions()
		
		self.assertTrue(len(cnfProductions) == 2)

		firstProduction = cnfProductions[0]
		secondProduction = cnfProductions[1]

		rhs1 = firstProduction.rhs()
		self.assertTrue(str(rhs1[0]) == 'X1')
		self.assertTrue(str(rhs1[1]) == 'C')

		rhs2 = secondProduction.rhs()
		self.assertTrue(str(rhs2[0]) == 'A')
		self.assertTrue(str(rhs2[1]) == 'B')

def main():
    unittest.main()

if __name__ == '__main__':
        main()