#Created on 3 Feb, 2014
#author: Olga Whelan


import nltk


class PCKY:
	def __init__(self):
		self.probGrammar = {}
		self.terminals = {}
		self.RHS = {}
		self.startSymbol = 'TOP'


        def putDS(self, tup):
        # getting the converted grammar and making it available
                self.probGrammar = tup[0]
		self.RHS = tup[1]
		self.terminals = tup[2]


	def runCKY(self, sentence):
		sent = nltk.word_tokenize(sentence)
		length = len(sent)
		
		matrix = [[0 for x in xrange(length+1)] for x in range(length)]	
	
		for jColumn in range(1, length+1):
		# the first 'for' fills the diagonal
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
					treesWithProbs.append([nltk.Tree(production, [lookUpWord]), prodProb])

				matrix[jColumn-1][jColumn] = treesWithProbs
			else:
				print "Error: word not in dictionary"

		print matrix

		for j in range(2, length+1):
			for i in range(j-2, -1, -1):

				treesWithProbs = []
				for k in range(i+1, j):
					trees1 = matrix[i][k][0]
					print matrix[i][k]
					print trees1
					trees2 = matrix[k][j][0]
					print trees2
					
					for tree1 in trees1:
						print tree1[0], tree1.node
						for tree2 in trees2:
							print tree2, tree2.node
							possibleLHS = str(tree1.node) + ' ' + str(tree2.node)
							if self.RHS.has_key(possibleLHS):
								productions = self.RHS[possibleLHS]

								for production in productions:
									for pair in self.probGrammar[production]:
										if pair[0] == possibleLHS:
											prodProb = pair[1]
									newProb = prodProb * matrix[i][k][1] * matrix[k][j][1]
									

									treesWithProbs.append([nltk.Tree(LHS, [tree1, tree2]), newProb])
				matrix[i][j] = treesWithProbs

		print matrix
#		
#		parseTrees = []
#		
#		for tree in matrix[0][length]:
#			if self.startSymbol in tree.node:	
#				parseTrees.append(tree)
#		return parseTrees
