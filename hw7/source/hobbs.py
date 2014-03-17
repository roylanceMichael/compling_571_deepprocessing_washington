# Mike Roylance - roylance@uw.edu
import sys
import nltk
import itemIndex
import rules
import traversableTree

# defining singleton rules
rules = rules.Rules()

class Hobbs:
	def __init__(self, firstTree, secondTree):
		self.foundPronouns = []

		self.firstTree = firstTree
		self.secondTree = secondTree

		self.firstTravTree = traversableTree.TraversableTree(self.firstTree, None)
		self.secondTravTree = traversableTree.TraversableTree(self.secondTree, self.firstTravTree)

	def searchForPronouns(self, travTree):
		# search self, then iterate through children
		if travTree.isPronoun(rules):
			self.foundPronouns.append(travTree)

		for childTree in travTree.children:
			self.searchForPronouns(childTree)

	def findPronouns(self):
		# we need to do this recursively



		pronouns = []
		self.processRules(rules.acceptablePronouns, self.secondTree, secondTree, pronouns)
		return pronouns

	def comparePronounInSentences(self, pronounIndex):
		for acceptedCandidate in self.comparePronounInTree(pronounIndex, self.secondTree):
			yield acceptedCandidate

		for acceptedCandidate in self.comparePronounInTree(pronounIndex, self.firstTree):
			yield acceptedCandidate

	def newComparePronoun(self, pronounIndex):
		# go to the NP directly preceding the pronoun
		pass


	def comparePronounInTree(self, pronounIndex, tree):
		potentialCandidates = self.processRules(rules.acceptableAntecedents, tree)

		for potentialCandidate in potentialCandidates:
			if rules.isPotentialAntecedent(pronounIndex, potentialCandidate):
				yield potentialCandidate

	def processRules(self, acceptableDictionary, directParent, rootTree, foundItems):
		treeIndex = 0
		for tree in directParent:
			node = str(tree.node)

			if node in acceptableDictionary:
				foundItems.append(itemIndex.ItemIndex(node, tree, directParent, rootTree, treeIndex, rules))

			treeIndex = treeIndex + 1

			self.processRules(acceptableDictionary, tree, rootTree, foundItems)

	def process(self):
		# let's print out when we find a POS in our pronouns
		pronouns = self.findPronouns()

		for pronoun in pronouns:
			# print out the pronoun and the corresponding parses
			yield "%s %s %s" % (pronoun.printItems(), self.printSentence(self.firstTree), self.printSentence(self.secondTree))

			# A) identify each parse tree node corresponding to 'X' in the algorithm, 
			# 	 writing out the corresponding NP or S (or SBAR) constituent.
			# B) identify each node proposed as an antecedent

			potentialAntecedents = self.comparePronounInSentences(pronoun)
			for potentialAntecedent in potentialAntecedents:
				yield potentialAntecedent.printSubTree()

				result = rules.indexAgreement(pronoun, potentialAntecedent)

				if len(result) == 0:
					# D) identify the accepted antecent.
					yield "Accept"

					# E) indicate whether the accepted antecedent is correct
					# F1) If the accepted antecedent is correct, do nothing more
					# F2) If the accepted antecedent is NOT correct, 
					# explain why and identify which of the syntactic and 
					# semantic preferences listed in the text (Slides: class 16, 10-11) would be required to correct this error.
					# If you take this coding route, you should output all the proposed antecedents, 
					# unless you want the added challenge of filtering for agreement.

					yield "Correct"
				else:
					# C) reject any proposed node ruled out by agreement
					yield "Reject - %s" % (result)

	def printSentence(self, tree):
		return str(tree.pprint(margin=500))