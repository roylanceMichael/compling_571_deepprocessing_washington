# created on 2 Feb, 2014
# by Michael Roylance, Olga Whelan


import nltk
import sys
import induceGrammar
import pcky
import tocnfOld

def parseTree(topTree):
	# topTree is a tuple
	if len(topTree[0]) == 1:
		return topTree[0][0] 

	actualTree = topTree[0]
	newString = ''

	for subTreeTuple in actualTree:
		newString = newString + '(' + subTreeTuple[0].node + ' '
		result = parseTree(subTreeTuple)
		newString = newString + str(result) + ')'
	
	return newString

def main():
        trFile = sys.argv[1]
	# create instance of class
	makeGram = induceGrammar.InduceGrammar()
	tocnfOldIns = tocnfOld.toCNF()

	productions = []

	for tree in open(trFile).xreadlines():
		rootTree = nltk.Tree.parse(tree)
		# rootTree.node - start symbol - assume that it is TOP and hardcode
		prods = rootTree.productions()

		for production in prods:
			# call function that would fill dicts: getListOfRules
			makeGram.fillDicts(str(production))
#	print makeGram.terminals
	pcfg = open("trained.pcfg", 'w+')
	pcfg.write(makeGram.buildPCFG())
	pcfg.close()

	# create instance of class
	pckyParser = pcky.PCKY()
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

		fullString = '(' + bestParse[0].node + ' '
		newString = parseTree(bestParse)
		fullString = fullString + newString + ')'
		
		print fullString.strip()
#		print bestParse		
		#parseFile.write(str(bestParse))
		#parseFile.write("\n")

                sent = exS.readline()

        exS.close()
	parseFile.close()



if __name__ == '__main__':
  main()
                              


