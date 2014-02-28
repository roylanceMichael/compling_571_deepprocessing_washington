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
		self.assertTrue(len(bestParse) > 1)
		
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
		self.assertTrue(len(bestParse) == 1)

		firstTree = bestParse[0]
		self.assertTrue(queryUtils.getPos(firstTree.node) == "S")

		secondTree = firstTree[0]
		self.assertTrue(queryUtils.getPos(secondTree.node) == "S")

		thirdTree = secondTree[0]
		self.assertTrue(queryUtils.getPos(thirdTree.node) == "NP")
		
		fourthTree = thirdTree[0]
		self.assertTrue(queryUtils.getPos(fourthTree.node) == "NNP")
		self.assertTrue(queryUtils.getTerminal(fourthTree) == "John")
		self.assertTrue(queryUtils.getNum(fourthTree.node) == "sg")

		fifthTree = secondTree[1]
		self.assertTrue(queryUtils.getPos(fifthTree.node) == "VP")
		self.assertTrue(queryUtils.getTerminal(fifthTree) == "thought")
		self.assertTrue(queryUtils.getTense(fifthTree.node) == "past")

		sixthTree = firstTree[1]
		self.assertTrue(queryUtils.getPos(sixthTree.node) == "IN")
		self.assertTrue(queryUtils.getTerminal(sixthTree) == "that")

		seventhTree = firstTree[2]
		self.assertTrue(queryUtils.getPos(seventhTree.node) == "S")

		eigthTree = seventhTree[0]
		self.assertTrue(queryUtils.getPos(eigthTree.node) == "NP")

		ninthTree = eigthTree[0]
		self.assertTrue(queryUtils.getPos(ninthTree.node) == "Det")
		self.assertTrue(queryUtils.getTerminal(ninthTree) == "the")

		tenthTree = eigthTree[1]
		self.assertTrue(queryUtils.getPos(tenthTree.node) == "N")
		self.assertTrue(queryUtils.getTerminal(tenthTree) == "book")
		self.assertTrue(queryUtils.getNum(tenthTree.node) == "sg")

		eleventhTree = seventhTree[1]
		self.assertTrue(queryUtils.getPos(eleventhTree.node) == "VP")
		self.assertTrue(queryUtils.getTerminal(eleventhTree) == "was")
		self.assertTrue(queryUtils.getTense(eleventhTree.node) == "past")

		twelthTree = seventhTree[2]
		self.assertTrue(queryUtils.getPos(twelthTree.node) == "VP")
		self.assertTrue(queryUtils.getTerminal(twelthTree) == "interesting")
		self.assertTrue(queryUtils.getTense(twelthTree.node) == "gerund")

	def test_ninthSentence(self):
		# arrange
		builder = parseResult.ParseResult("../docs/grammar.fcfg")
		sentence = "John thought the book" 

		# act
		bestParse = builder.build(sentence)

		# assert
		self.assertTrue(len(bestParse) == 0)

	def test_tenthSentence(self):
		# arrange
		builder = parseResult.ParseResult("../docs/grammar.fcfg")
		sentence = "Mary put the book ." 

		# act
		bestParse = builder.build(sentence)

		# assert
		self.assertTrue(len(bestParse) == 0)

	def test_11Sentence(self):
		# arrange
		builder = parseResult.ParseResult("../docs/grammar.fcfg")
		sentence = "Mary put the book on the shelf ." 

		# act
		bestParse = builder.build(sentence)

		# assert
		self.assertTrue(len(bestParse) == 1)

		firstTree = bestParse[0]
		self.assertTrue(queryUtils.getPos(firstTree.node) == "S")

		secondTree = firstTree[0]
		self.assertTrue(queryUtils.getPos(secondTree.node) == "NP")

		thirdTree = secondTree[0]
		self.assertTrue(queryUtils.getPos(thirdTree.node) == "NNP")
		self.assertTrue(queryUtils.getTerminal(thirdTree) == "Mary")
		self.assertTrue(queryUtils.getNum(thirdTree.node) == "sg")
		
		fourthTree = firstTree[1]
		self.assertTrue(queryUtils.getPos(fourthTree.node) == "VP")

		fifthTree = fourthTree[0]
		self.assertTrue(queryUtils.getPos(fifthTree.node) == "VP")
		self.assertTrue(queryUtils.getTerminal(fifthTree) == "put")
		self.assertTrue(queryUtils.getTense(fifthTree.node) == "past")

		sixthTree = fourthTree[1]
		self.assertTrue(queryUtils.getPos(sixthTree.node) == "NP")

		seventhTree = sixthTree[0]
		self.assertTrue(queryUtils.getPos(seventhTree.node) == "Det")
		self.assertTrue(queryUtils.getTerminal(seventhTree) == "the")

		eighthTree = sixthTree[1]
		self.assertTrue(queryUtils.getPos(eighthTree.node) == "N")
		self.assertTrue(queryUtils.getTerminal(eighthTree) == "book")
		self.assertTrue(queryUtils.getNum(eighthTree.node) == "sg")

		ninthTree = fourthTree[2]
		self.assertTrue(queryUtils.getPos(ninthTree.node) == "PP")

		tenthTree = ninthTree[0]
		self.assertTrue(queryUtils.getPos(tenthTree.node) == "P")
		self.assertTrue(queryUtils.getTerminal(tenthTree) == "on")

		eleventhTree = ninthTree[1]
		self.assertTrue(queryUtils.getPos(eleventhTree.node) == "NP")

		twelthTree = eleventhTree[0]
		self.assertTrue(queryUtils.getPos(twelthTree.node) == "Det")
		self.assertTrue(queryUtils.getTerminal(twelthTree) == "the")

		thirteenthTree = eleventhTree[1]
		self.assertTrue(queryUtils.getPos(thirteenthTree.node) == "N")
		self.assertTrue(queryUtils.getTerminal(thirteenthTree) == "shelf")
		self.assertTrue(queryUtils.getNum(thirteenthTree.node) == "sg")

	def test_12Sentence(self):
		# arrange
		builder = parseResult.ParseResult("../docs/grammar.fcfg")
		sentence = "did Mary put the book on the shelf ?" 

		# act
		bestParse = builder.build(sentence)

		# assert
		self.assertTrue(len(bestParse) == 1)

	def test_13Sentence(self):
		# arrange
		builder = parseResult.ParseResult("../docs/grammar.fcfg")
		sentence = "put Mary the book on the shelf ?" 

		# act
		bestParse = builder.build(sentence)

		# assert
		self.assertTrue(len(bestParse) == 0)

	def test_14Sentence(self):
		# arrange
		builder = parseResult.ParseResult("../docs/grammar.fcfg")
		sentence = "what did Mary put on the shelf ?" 

		# act
		bestParse = builder.build(sentence)

		# assert
		self.assertTrue(len(bestParse) == 1)

	def test_15Sentence(self):
		# arrange
		builder = parseResult.ParseResult("../docs/grammar.fcfg")
		sentence = "what did Mary put ?" 

		# act
		bestParse = builder.build(sentence)

		# assert
		self.assertTrue(len(bestParse) == 0)

	def test_16Sentence(self):
		# arrange
		builder = parseResult.ParseResult("../docs/grammar.fcfg")
		sentence = "what does John know ?" 

		# act
		bestParse = builder.build(sentence)

		# assert
		self.assertTrue(len(bestParse) == 1)

	def test_17Sentence(self):
		# arrange
		builder = parseResult.ParseResult("../docs/grammar.fcfg")
		sentence = "what does Mary think John knows ?" 

		# act
		bestParse = builder.build(sentence)

		# assert
		self.assertTrue(len(bestParse) == 1)

	def test_18Sentence(self):
		# arrange
		builder = parseResult.ParseResult("../docs/grammar.fcfg")
		sentence = "the farmer loaded the cart with sand ." 

		# act
		bestParse = builder.build(sentence)

		# assert
		self.assertTrue(len(bestParse) > 1)

	def test_19Sentence(self):
		# arrange
		builder = parseResult.ParseResult("../docs/grammar.fcfg")
		sentence = "the farmer loaded the cart with sand ." 

		# act
		bestParse = builder.build(sentence)

		# assert
		self.assertTrue(len(bestParse) > 1)

	def test_20Sentence(self):
		# arrange
		builder = parseResult.ParseResult("../docs/grammar.fcfg")
		sentence = "the farmer loaded sand into the cart ." 

		# act
		bestParse = builder.build(sentence)

		# assert
		self.assertTrue(len(bestParse) > 1)

	def test_21Sentence(self):
		# arrange
		builder = parseResult.ParseResult("../docs/grammar.fcfg")
		sentence = "the farmer filled sand into the cart ." 

		# act
		bestParse = builder.build(sentence)

		# assert
		self.assertTrue(len(bestParse) > 1)

	def test_21Sentence(self):
		# arrange
		builder = parseResult.ParseResult("../docs/grammar.fcfg")
		sentence = "the farmer filled the cart with sand ." 

		# act
		bestParse = builder.build(sentence)

		# assert
		self.assertTrue(len(bestParse) > 1)

	def test_22Sentence(self):
		# arrange
		builder = parseResult.ParseResult("../docs/grammar.fcfg")
		sentence = "Mary saw herself ." 

		# act
		bestParse = builder.build(sentence)

		# assert
		self.assertTrue(len(bestParse) == 1)

	def test_23Sentence(self):
		# arrange
		builder = parseResult.ParseResult("../docs/grammar.fcfg")
		sentence = "Mary saw herself ." 

		# act
		bestParse = builder.build(sentence)

		# assert
		self.assertTrue(len(bestParse) == 1)

	def test_24Sentence(self):
		# arrange
		builder = parseResult.ParseResult("../docs/grammar.fcfg")
		sentence = "John saw himself ." 

		# act
		bestParse = builder.build(sentence)

		# assert
		self.assertTrue(len(bestParse) == 1)

	def test_25Sentence(self):
		# arrange
		builder = parseResult.ParseResult("../docs/grammar.fcfg")
		sentence = "John reached the summit on Tuesday ." 

		# act
		bestParse = builder.build(sentence)

		# assert
		self.assertTrue(len(bestParse) > 1)

	def test_26Sentence(self):
		# arrange
		builder = parseResult.ParseResult("../docs/grammar.fcfg")
		sentence = "Mary reached the summit for five minutes ." 

		# act
		bestParse = builder.build(sentence)

		# assert
		self.assertTrue(len(bestParse) > 1)

	def test_27Sentence(self):
		# arrange
		builder = parseResult.ParseResult("../docs/grammar.fcfg")
		sentence = "John walked on Tuesday ." 

		# act
		bestParse = builder.build(sentence)

		# assert
		self.assertTrue(len(bestParse) > 1)

	def test_28Sentence(self):
		# arrange
		builder = parseResult.ParseResult("../docs/grammar.fcfg")
		sentence = "Mary walked for five minutes ." 

		# act
		bestParse = builder.build(sentence)

		# assert
		self.assertTrue(len(bestParse) > 1)

def main():
    unittest.main()

if __name__ == '__main__':
        main()