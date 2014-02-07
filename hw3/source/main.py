# created on 2 Feb, 2014
# by Michael Roylance, Olga Whelan


import nltk
import sys
import re
import induceGrammar
import pcky

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

	exampleSents = sys.argv[2]
        exS = open(exampleSents, 'rU')

#	read input sentences from file one by one
	parseFile = open("parses.hyp", 'w+')
        sent = exS.readline()
        while sent:

		bestParse = pckyParser.runCKY(sent)
		parseFile.write(bestParse.strip())
		parseFile.write("\n")

                sent = exS.readline()

        exS.close()
	parseFile.close()

if __name__ == '__main__':
  main()
