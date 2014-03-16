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
		for acceptedCandidate in self.comparePronounInTree(pronounIndex, self.secondTree):
			yield acceptedCandidate

		for acceptedCandidate in self.comparePronounInTree(pronounIndex, self.firstTree):
			yield acceptedCandidate

	def comparePronounInTree(self, pronounIndex, tree):
		potentialCandidates = self.processRules(rules.acceptableAntecedents, tree)

		for potentialCandidate in potentialCandidates:
			if rules.isPotentialAntecedent(pronounIndex, potentialCandidate):
				yield potentialCandidate

	def processRules(self, acceptableDictionary, rootTree):
		treeIndex = 0
		for tree in rootTree.subtrees():
			node = str(tree.node)

			if node in acceptableDictionary:
				yield itemIndex.ItemIndex(node, tree, rootTree, treeIndex, rules)

			treeIndex = treeIndex + 1

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