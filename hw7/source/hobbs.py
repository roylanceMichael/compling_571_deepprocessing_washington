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
		self.proposedAntecedents = []

		self.firstTree = firstTree
		self.secondTree = secondTree

		self.firstTravTree = traversableTree.TraversableTree(self.firstTree, None, rules)
		self.secondTravTree = traversableTree.TraversableTree(self.secondTree, self.firstTravTree, rules)

		self.searchForPronouns(self.secondTravTree)

	def searchForPronouns(self, travTree):
		# search self, then iterate through children
		if travTree.isPronoun:
			self.foundPronouns.append(travTree)

		for childTree in travTree.children:
			self.searchForPronouns(childTree)

	def findAntecedents(self):
		for pronounTravTree in self.foundPronouns:
			# print out the pronoun and the corresponding parses
			yield "%s %s %s" % (pronounTravTree.printItems(), 
				self.printSentence(self.firstTree), 
				self.printSentence(self.secondTree))

			p = {}
			# Begin at NP immediately dominating the pronoun
			currentNp = self.findNpOrS(pronounTravTree)
			p[currentNp] = None
			nextNpOrS = None

			while currentNp != None:
				# Climb tree to NP or S: X=node, p=path
				nextNpOrS = self.findNpOrS(currentNp)
				p[nextNpOrS] = None

				if nextNpOrS == None:
					currentNp = None
					continue

				for result in self.determineAntecedents(nextNpOrS, p, pronounTravTree):
					yield result

				currentNp = nextNpOrS

	def determineAntecedents(self, X, p, pronoun):
		# if X is NP and not through p, then propose
		if X.pos == rules.np and not X.hasPronouns:
			# set in path
			p[X] = None

			for result in self.printComparison(pronoun, X):
				yield result

		# print out X if it is S or SBAR
		if X.pos == rules.sbar or X.pos == rules.s:
			# this is X
			yield self.printSentence(X.tree)

		for child in X.children:
			# if we hit our path, move on
			if child in p:
				continue

			for result in self.determineAntecedents(child, p, pronoun):
				yield result

	def findNpOrS(self, travTree):
		nextNpOrS = None
		currentNode = travTree

		while currentNode != None:
			if currentNode.parent == None:
				currentNode = None
				continue

			if (currentNode.parent.pos in rules.acceptableAntecedents):
				nextNpOrS = currentNode.parent
				currentNode = None
				continue

			currentNode = currentNode.parent

		return nextNpOrS

	def printComparison(self, pronoun, proposedAntecedent):
		# comparing NP
		yield proposedAntecedent.printTree()

		result = rules.treeAgreement(pronoun, proposedAntecedent)

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

			# this will be added manually
			# yield "Correct"
		else:
			# C) reject any proposed node ruled out by agreement
			yield "Reject - %s" % (result)			

	def printSentence(self, tree):
		return str(tree.pprint(margin=500))