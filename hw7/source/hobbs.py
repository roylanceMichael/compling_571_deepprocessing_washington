# Mike Roylance - roylance@uw.edu
import sys
import nltk
import itemIndex
import rules

# defining singleton rules
rules = rules.Rules()

class Hobbs:
	def __init__(self, firstTree, secondTree):
		self.firstTree = firstTree
		self.secondTree = secondTree

	def findPronouns(self):
		return self.processRules(rules.acceptablePronouns, self.secondTree)

	def comparePronounInSentences(self, pronounIndex):
		foundCandidateInSecondSentence = False
		acceptedCandidates = self.comparePronounInTree(pronounIndex, self.secondTree)

		for acceptedCandidate in acceptedCandidates:
				yield acceptedCandidate
				foundCandidateInSecondSentence = True
		
		if foundCandidateInSecondSentence:
			return

		for acceptedCandidate in self.comparePronounInTree(pronounIndex, self.firstTree):
			yield acceptedCandidate

	def comparePronounInTree(self, pronounIndex, tree):
		potentialCandidates = self.processRules(rules.acceptableAntecedents, tree)

		for potentialCandidate in potentialCandidates:
			if rules.indexAgreement(pronounIndex, potentialCandidate):
				yield (pronounIndex, potentialCandidate)

	def processRules(self, acceptableDictionary, rootTree):
		treeIndex = 0
		for tree in rootTree.subtrees():
			node = str(tree.node)

			if node in acceptableDictionary:
				pos = tree.pos()[0][0]

				yield itemIndex.ItemIndex(pos, node, tree, rootTree, treeIndex)

			treeIndex = treeIndex + 1

	def process(self):
		# let's print out when we find a POS in our pronouns

		self.processSubTree(self.secondTree)

	def processSubTree(self, tree):
		subTrees = tree.subtrees()

		for tree in subTrees:
			print '----'
			print len(tree)
			print tree.pos()
			print tree.node
			print tree

			# self.processSubTree(tree)