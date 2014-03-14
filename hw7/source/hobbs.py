# Mike Roylance - roylance@uw.edu
import sys
import nltk

class Hobbs:
	def __init__(self, firstTree, secondTree):
		self.firstTree = firstTree
		self.secondTree = secondTree

		# hard coding the pronouns, as found in ../docs/grammar.cfg
		self.pronouns = {}
		self.pronouns["PRP"] = None
		self.pronouns["PossPro"] = None

	def findPronouns(self):
		foundPronouns = []
		for tree in self.secondTree.subtrees():
			node = str(tree.node)

			if node in self.pronouns:
				pronoun = tree.pos()[0][0]

				foundPronouns.append(pronoun) 

		return foundPronouns

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