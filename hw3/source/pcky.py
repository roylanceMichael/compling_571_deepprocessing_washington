# Created on 3 Feb, 2014
# by Michael Roylance, Olga Whelan


from operator import itemgetter
import nltk


class PCKY:
	def __init__(self, startSymbol):
		self.probGrammar = {}
		self.terminals = {}
		self.nonTerminalsWithTerminals = []
		self.RHS = {}
		self.startSymbol = startSymbol

	def parseTree(self, topTree):
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
			result = self.parseTree(subTreeTuple)
			newString = newString + str(result) + ')'
		
		return newString

	def putDS(self, tup):
	# getting the converted grammar and making it available
		self.probGrammar = tup[0]
		self.RHS = tup[1]
		self.terminals = tup[2]
		tempNonTerminals = {}

		# self.terminals => {'conjugate' => ['VB', 'VP'] }
		for terminal in self.terminals:
			# ['VP', 'VB']
			nonTerminals = self.terminals[terminal]
			for nonTerminal in nonTerminals:

				# nonTerminal => 'VB'
				if nonTerminal not in tempNonTerminals:
					tempNonTerminals[nonTerminal] = None
					self.nonTerminalsWithTerminals.append(nonTerminal)

		# experiment for implementing parent annotation
		#for key in self.probGrammar:
		#	replaceList = []
		#	for rhs in self.probGrammar[key]:
		#		splitRhs = rhs[0].split(' ')

		#		if (len(splitRhs) == 2 and 
		#			splitRhs[0] not in tempNonTerminals and 
		#			splitRhs[1] not in tempNonTerminals):
		#			newRhs1 = splitRhs[0] + "^" + key
		#			newRhs2 = splitRhs[1] + "^" + key
		#			replaceList.append((newRhs1 + " " + newRhs2, rhs[1]))
		#		else:
		#			replaceList.append(rhs)

		#	self.probGrammar[key] = replaceList

	def runCKY(self, sentence):
	# the heart of the project
		sent = nltk.word_tokenize(sentence)
		length = len(sent)
		
		matrix = [[0 for x in xrange(length+1)] for x in range(length)]	
	
		for jColumn in range(1, length+1):
		# the first 'for' fills the diagonal
			lookUpWord = ""

			# this is for when a ' exists in the key
			if "'" in sent[jColumn-1]:
				lookUpWord = '"' + sent[jColumn-1] + '"'
			else:
				lookUpWord = "'" + sent[jColumn-1] + "'"

			# get rules from terminal dictionary
			treesWithProbs = []
			if self.terminals.has_key(lookUpWord):
				productions = self.terminals[lookUpWord]

				for production in productions:	
				# and get the probability
					for pair in self.probGrammar[production]:
						if pair[0] == lookUpWord:
							prodProb = pair[1]
					treesWithProbs.append((nltk.Tree(production, [lookUpWord]), prodProb))

				matrix[jColumn-1][jColumn] = treesWithProbs
			else:

				#for nonTerminal in self.nonTerminalsWithTerminals:
				#	treesWithProbs.append((nltk.Tree(nonTerminal, [lookUpWord]), 0.0001))

				matrix[jColumn-1][jColumn] = []#treesWithProbs

		for j in range(2, length+1):
			for i in range(j-2, -1, -1):

				treesWithProbs = []	# list of tuples (tree, prob)
				for k in range(i+1, j):
					trees1 = matrix[i][k]

					trees2 = matrix[k][j]

					for tree1 in trees1:

						for tree2 in trees2:

							possibleLHS = str(tree1[0].node) + ' ' + str(tree2[0].node)	# getting the two non-terminals to look up in the dictionary for corresponding lhs

							if self.RHS.has_key(possibleLHS):

								productions = self.RHS[possibleLHS]

								for production in productions:
									# here we're just looking for a tuple containing the right production - there's only one we need; and there will only be one probability
									# we don't really need to loop through all the pairs, but how to get to it without looping?
									for pair in self.probGrammar[production]:

										if pair[0] == possibleLHS:

											prodProb = pair[1]
									newProb = prodProb * tree1[1] * tree2[1]

									treesWithProbs.append((nltk.Tree(production, [tree1, tree2]), newProb))

				matrix[i][j] = treesWithProbs

		parseTrees = []

		for treeProbTup in matrix[0][length]:
			if self.startSymbol in treeProbTup[0].node:	
				parseTrees.append(treeProbTup)

		if parseTrees == []:
			return ''

		bestParse = max(parseTrees, key = itemgetter(1))	# the best parse has the maximum probability

		fullString = '(' + bestParse[0].node + ' '
		newString = self.parseTree(bestParse)	# need to clean up our best parse to make it ready for evalb
		fullString = fullString + newString + ')'	
		return fullString
