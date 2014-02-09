# Mike Roylance - roylance@uw.edu
import unittest
import nltk
import parseResult
import queryUtils

class FeatureGrammar(unittest.TestCase):
	def test_loadExampleFeatureGrammar(self):
		# arrange
		# act
		cp = nltk.load_parser("file:../docs/example_grammar.fcfg")

		# assert
		self.assertTrue(cp != None)

class ParseResult(unittest.TestCase):
	def test_parseSentenceSingle(self):
		# arrange
		builder = parseResult.ParseResult("../docs/example_grammar.fcfg")
		sentence = "Kim likes children" 

		# act
		bestParse = builder.build(sentence)

		# assert
		self.assertTrue(bestParse != None)
		
		# get the S tree
		firstTree = bestParse[0]
		self.assertTrue(queryUtils.getPos(firstTree.node) == "S")

		secondTree = firstTree[0]
		self.assertTrue(queryUtils.getPos(secondTree.node) == "NP")
		self.assertTrue(queryUtils.getTerminal(secondTree) == "Kim")

		thirdTree = firstTree[1]
		self.assertTrue(queryUtils.getPos(thirdTree.node) == "VP")

		fourthTree = thirdTree[0]
		self.assertTrue(queryUtils.getPos(fourthTree.node) == "V")
		self.assertTrue(queryUtils.getTerminal(fourthTree) == "likes")

		fifthTree = thirdTree[1]
		self.assertTrue(queryUtils.getPos(fifthTree.node) == "NP")
		self.assertTrue(queryUtils.getTerminal(fifthTree) == "children")
		
	def test_firstSentence(self):
		# arrange
		builder = parseResult.ParseResult("../docs/grammar.fcfg")
		sentence = "the dogs bark ." 

		# act
		bestParse = builder.build(sentence)

		# assert
		self.assertTrue(len(bestParse) == 1)
		
		firstTree = bestParse[0]
		self.assertTrue(queryUtils.getPos(firstTree.node) == "S")

		secondTree = firstTree[0]
		self.assertTrue(queryUtils.getPos(secondTree.node) == "NP")

		thirdTree = secondTree[0]
		self.assertTrue(queryUtils.getPos(thirdTree.node) == "Det")
		self.assertTrue(queryUtils.getTerminal(thirdTree) == "the")

		fourthTree = secondTree[1]
		self.assertTrue(queryUtils.getPos(fourthTree.node) == "N")
		self.assertTrue(queryUtils.getTerminal(fourthTree) == "dogs")
		self.assertTrue(queryUtils.getNum(fourthTree.node) == "pl")

		fifthTree = firstTree[1]
		self.assertTrue(queryUtils.getPos(fifthTree.node) == "VP")
		self.assertTrue(queryUtils.getTerminal(fifthTree) == "bark")
		self.assertTrue(queryUtils.getNum(fifthTree.node) == "pl")

		sixthTree = firstTree[2]
		self.assertTrue(queryUtils.getPos(sixthTree.node) == "PUNC")
		self.assertTrue(queryUtils.getTerminal(sixthTree) == ".")

	def test_secondSentence(self):
		# arrange
		builder = parseResult.ParseResult("../docs/grammar.fcfg")
		sentence = "the dog barks ." 

		# act
		bestParse = builder.build(sentence)

		# assert
		self.assertTrue(len(bestParse) == 1)
		
		firstTree = bestParse[0]
		self.assertTrue(queryUtils.getPos(firstTree.node) == "S")

		secondTree = firstTree[0]
		self.assertTrue(queryUtils.getPos(secondTree.node) == "NP")

		thirdTree = secondTree[0]
		self.assertTrue(queryUtils.getPos(thirdTree.node) == "Det")
		self.assertTrue(queryUtils.getTerminal(thirdTree) == "the")

		fourthTree = secondTree[1]
		self.assertTrue(queryUtils.getPos(fourthTree.node) == "N")
		self.assertTrue(queryUtils.getTerminal(fourthTree) == "dog")
		self.assertTrue(queryUtils.getNum(fourthTree.node) == "sg")

		fifthTree = firstTree[1]
		self.assertTrue(queryUtils.getPos(fifthTree.node) == "VP")
		self.assertTrue(queryUtils.getTerminal(fifthTree) == "barks")
		self.assertTrue(queryUtils.getNum(fifthTree.node) == "sg")

		sixthTree = firstTree[2]
		self.assertTrue(queryUtils.getPos(sixthTree.node) == "PUNC")
		self.assertTrue(queryUtils.getTerminal(sixthTree) == ".")

	def test_thirdSentence(self):
		# arrange
		builder = parseResult.ParseResult("../docs/grammar.fcfg")
		sentence = "the dog bark ." 

		# act
		bestParse = builder.build(sentence)

		# assert
		self.assertTrue(len(bestParse) == 0)

	def test_fourthSentence(self):
		# arrange
		builder = parseResult.ParseResult("../docs/grammar.fcfg")
		sentence = "the dogs barks ." 

		# act
		bestParse = builder.build(sentence)

		# assert
		self.assertTrue(len(bestParse) == 0)

	def test_fifthSentence(self):
		# arrange
		builder = parseResult.ParseResult("../docs/grammar.fcfg")
		sentence = "the dog bark ." 

		# act
		bestParse = builder.build(sentence)

		# assert
		self.assertTrue(len(bestParse) == 0)

	def test_sixthSentence(self):
		# arrange
		builder = parseResult.ParseResult("../docs/grammar.fcfg")
		sentence = "dog barks ." 

		# act
		bestParse = builder.build(sentence)

		# assert
		self.assertTrue(len(bestParse) == 1)
		
		firstTree = bestParse[0]
		self.assertTrue(queryUtils.getPos(firstTree.node) == "S")

		secondTree = firstTree[0]
		self.assertTrue(queryUtils.getPos(secondTree.node) == "NP")

		fourthTree = secondTree[0]
		self.assertTrue(queryUtils.getPos(fourthTree.node) == "N")
		self.assertTrue(queryUtils.getTerminal(fourthTree) == "dog")
		self.assertTrue(queryUtils.getNum(fourthTree.node) == "sg")

		fifthTree = firstTree[1]
		self.assertTrue(queryUtils.getPos(fifthTree.node) == "VP")
		self.assertTrue(queryUtils.getTerminal(fifthTree) == "barks")
		self.assertTrue(queryUtils.getNum(fifthTree.node) == "sg")

		sixthTree = firstTree[2]
		self.assertTrue(queryUtils.getPos(sixthTree.node) == "PUNC")
		self.assertTrue(queryUtils.getTerminal(sixthTree) == ".")

	def test_seventhSentence(self):
		# arrange
		builder = parseResult.ParseResult("../docs/grammar.fcfg")
		sentence = "the dogs bark the cats ." 

		# act
		bestParse = builder.build(sentence)

		# assert
		self.assertTrue(len(bestParse) == 0)

	def test_eigthSentence(self):
		# arrange
		builder = parseResult.ParseResult("../docs/grammar.fcfg")
		sentence = "John thought that the book was interesting ." 

		# act
		bestParse = builder.build(sentence)

		# assert
		self.assertTrue(len(bestParse) == 0)

def main():
    unittest.main()

if __name__ == '__main__':
        main()