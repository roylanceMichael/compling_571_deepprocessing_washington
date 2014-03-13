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

	def process(self):
		print self.firstTree
		print self.secondTree

		# TODO
		# start with target pronoun (in secondtree)
		# climb parse tree to S root (of firsttree)
		# for each NP or S
		# breadth first search, left to right, of children

		# so ya, I've done this before... let's finish tomorrow...