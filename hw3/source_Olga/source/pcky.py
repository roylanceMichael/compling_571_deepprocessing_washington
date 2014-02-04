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
					treesWithProbs.append((nltk.Tree(production, [lookUpWord]), prodProb))

				matrix[jColumn-1][jColumn] = treesWithProbs
			else:
				print "Error: word not in dictionary"

		#print matrix
		for item in matrix:
			print item

		for j in range(2, length+1):
			for i in range(j-2, -1, -1):

				treesWithProbs = []
				for k in range(i+1, j):
					trees1 = matrix[i][k]
					# print matrix[i][k]
					#print 'trees1:'
					#print trees1
					trees2 = matrix[k][j]
					
					#print 'trees2:'
					#print trees2

					if type(trees1) == type(1):
						continue
					
					for tree1 in trees1:
						#print 'tree1, tree1[0].node, tree2'
						#print tree1, tree1[0].node
						#print trees2

						if type(trees2) == type(1):
							continue

						for tree2 in trees2:
							#print 'test'
							# print tree2, tree2[0].node
							#print 'test - done'
							possibleLHS = str(tree1[0].node) + ' ' + str(tree2[0].node)

							if self.RHS.has_key(possibleLHS):
								print possibleLHS

								productions = self.RHS[possibleLHS]
								print 'found productions'
								print productions

								for production in productions:
									for pair in self.probGrammar[production]:
										print 'pair[0] here with possibleLHS:'
										print pair[0]
										print possibleLHS

										if pair[0] == possibleLHS:
											print 'found pair!'
											prodProb = pair[1]
									newProb = prodProb * tree1[1] * tree2[1]
									

									treesWithProbs.append((nltk.Tree(possibleLHS, [tree1, tree2]), newProb))
				matrix[i][j] = treesWithProbs

		print 'final matrix: '

		for item in matrix:
			print item
		
		#parseTrees = []
		
		#for tree in matrix[0][length]:
		#	if self.startSymbol in tree.node:	
		#		parseTrees.append(tree)
		#return parseTrees
