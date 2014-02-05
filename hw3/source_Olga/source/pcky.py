# Created on 3 Feb, 2014
# by Michael Roylance, Olga Whelan


from operator import itemgetter
import nltk


class PCKY:
	def __init__(self, startSymbol):
		self.probGrammar = {}
		self.terminals = {}
		self.RHS = {}
		self.startSymbol = startSymbol


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
				matrix[jColumn-1][jColumn] = []

		for j in range(2, length+1):
			for i in range(j-2, -1, -1):

				treesWithProbs = []
				for k in range(i+1, j):
					trees1 = matrix[i][k]
					# print matrix[i][k]
					#print trees1
					trees2 = matrix[k][j]

					for tree1 in trees1:
						#print 'tree1, tree1[0].node, tree2'
						#print tree1, tree1[0].node

						for tree2 in trees2:
							# print tree2, tree2[0].node
							possibleLHS = str(tree1[0].node) + ' ' + str(tree2[0].node)
#							print "pair up the nodes and get: ", possibleLHS

							if self.RHS.has_key(possibleLHS):

								productions = self.RHS[possibleLHS]
#								print productions

								for production in productions:
									# here we're just looking for a tuple containing the right production
									# there's only one we need; and there will only be one probability
									# we don't really need to loop through all the pairs
									# but how to get to it without looping?
									for pair in self.probGrammar[production]:
#										print 'pair[0] here with possibleLHS:'

										if pair[0] == possibleLHS:
#											print 'found pair!'
											prodProb = pair[1]
									newProb = prodProb * tree1[1] * tree2[1]
									

									treesWithProbs.append((nltk.Tree(production, [tree1, tree2]), newProb))
				matrix[i][j] = treesWithProbs

#		print 'final matrix: '
#		print matrix[0][-1]
		parseTrees = []
		
		for treeProbTup in matrix[0][length]:
			if self.startSymbol in treeProbTup[0].node:	
				parseTrees.append(treeProbTup)

#		print "\n\n\n"
		if parseTrees == []:
			return ''

		bestParse = max(parseTrees, key = itemgetter(1))
		# cannot print it as a tree because of probabilities on each level...
#		print bestParse

		return bestParse
