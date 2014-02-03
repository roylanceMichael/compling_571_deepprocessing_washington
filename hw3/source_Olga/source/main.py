import nltk
import sys
import induceGrammar
import pcky


def main():
        trFile = sys.argv[1]
	# create instance of class
	makeGram = induceGrammar.InduceGrammar()

	productions = []

	for tree in open(trFile).xreadlines():
		rootTree = nltk.Tree.parse(tree)
		# rootTree.node - start symbol - assume that it is TOP and hardcode
		prods = rootTree.productions()

		for production in prods:
	#		print production
			# call function that would fill dicts: getListOfRules
			makeGram.fillDicts(str(production))
#	print makeGram.rules
#	print makeGram.terminals
	pcfg = open("trained.pcfg", 'w+')
	pcfg.write(makeGram.buildPCFG())
	pcfg.close()

	# create instance of class
	pckyParser = pcky.PCKY()
	pckyParser.putDS(makeGram.getDS())
#	print pckyParser.probGrammar
#	print pckyParser.terminals

#	print makeGram.rules

	exampleSents = sys.argv[2]
        exS = open(exampleSents, 'rU')

#	read input sentences from file one by one
        sent = exS.readline()
        while sent:
		print sent
		print pckyParser.runCKY(sent)
#		parseTrees = pckyParser.runCKY(sent)
#		for tree in parseTrees:
#			print tree,  "\n"
#		print "number of parses: ", len(parseTrees), "\n"

                sent = exS.readline()

        exS.close()



if __name__ == '__main__':
  main()
                              


