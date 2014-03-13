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