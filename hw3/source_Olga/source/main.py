# created on 2 Feb, 2014
# by Michael Roylance, Olga Whelan


import nltk
import sys
import re
import induceGrammar
import pcky


def parseTree(topTree):
# clean out the output tree; take out nltk formatting and the probabilities from each level 
	# topTree is a tuple
	if len(topTree[0]) == 1:
		terminalVal = topTree[0][0]

		if ((terminalVal[0] == "'" and terminalVal[-1] == "'") or 
			(terminalVal[0] == '"' and terminalVal[-1] == '"')):
			return terminalVal[1:-1]
		
		return terminalVal

	actualTree = topTree[0]
	newString = ''

	for subTreeTuple in actualTree:
		newString = newString + '(' + subTreeTuple[0].node + ' '
		result = parseTree(subTreeTuple)
		newString = newString + str(result) + ')'
	
	return newString

def main():
        trFile = sys.argv[1]
	# create instance of class InduceGrammar
	makeGram = induceGrammar.InduceGrammar()

	productions = []

	for tree in open(trFile).xreadlines():
		rootTree = nltk.Tree.parse(tree)
		prods = rootTree.productions()
		
		startSymbol = str(prods[0].lhs())

		for production in prods:
			# call function that would fill useful data structures
			makeGram.fillDicts(str(production))
	pcfg = open("trained.pcfg", 'w+')
	pcfg.write(makeGram.buildPCFG())
	pcfg.close()

	# create instance of class PCKY
	pckyParser = pcky.PCKY(startSymbol)
	pckyParser.putDS(makeGram.getDS())
#	print pckyParser.terminals

	exampleSents = sys.argv[2]
        exS = open(exampleSents, 'rU')

#	read input sentences from file one by one
	parseFile = open("parses.hyp", 'w+')
        sent = exS.readline()
        while sent:
#		print sent
		bestParse = pckyParser.runCKY(sent)

		if len(bestParse) == 0:
			print sent
			parseFile.write("\n")
			sent = exS.readline()
			continue

		fullString = '(' + bestParse[0].node + ' '
		newString = parseTree(bestParse)	# need to clean up our best parse to make it ready for evalb
		fullString = fullString + newString + ')'
#		print bestParse		
		parseFile.write(fullString.strip())
		parseFile.write("\n")

                sent = exS.readline()

        exS.close()
	parseFile.close()



if __name__ == '__main__':
  main()
