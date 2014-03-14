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
		potentialCandidates = self.processRules(rules.acceptableAntecedents, self.firstTree)

		acceptedCandidates = []

		for potentialCandidate in potentialCandidates:
			if rules.indexAgreement(pronounIndex, potentialCandidate):
				acceptedCandidates.append((pronounIndex, potentialCandidate))

		return acceptedCandidates

	def processRules(self, acceptableDictionary, rootTree):
		items = []

		for tree in rootTree.subtrees():
			node = str(tree.node)

			if node in acceptableDictionary:
				pos = tree.pos()[0][0]

				items.append(itemIndex.ItemIndex(pos, node, tree, rootTree))

		return items

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