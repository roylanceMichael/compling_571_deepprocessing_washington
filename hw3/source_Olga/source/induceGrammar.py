from __future__ import division
import nltk
import re


class InduceGrammar:
	def __init__(self):
		self.rules = {}
		self.lhs = {}
		self.terminals = {}


	def LHS_RHS(self, line):
	# get tuples (lhs, rhs) - there turns out to be a much simpler way to do it!
		match = re.search(r'(\w+\'*)\s*(->|=>|>)(.+$)', line)
		if match:
			lhs = match.group(1)
			all_rhs = match.group(3)
		else:
			print 'match not found'

		all_rhs = all_rhs.strip()

		tup = (lhs, all_rhs)
		return tup


	def fillDicts(self, line):
	# fill the big dictionary {lhs: [(rhs1, prob), (rhs2, prob),..],..}
		tup = self.LHS_RHS(line)

		if tup[0] in self.rules:
			listofprod = []

			for prod in self.rules[tup[0]]:
				listofprod.append(prod[0])
			for prod in self.rules[tup[0]]:
				if tup[1] in prod[0]:

					prod[1] = prod[1] + 1
			if tup[1] not in listofprod:
				newProd = [tup[1], 1]
				self.rules[tup[0]].append(newProd)
		else:
			self.rules[tup[0]] = [[tup[1], 1]]
		
		self.getLHSAndTerminals(tup)


	def getLHSAndTerminals(self, tup):
	# get dictionaries of non-terminals {NONT1: ['term1', 'term2',..], NONT2 : [], ...  }
	# and terminals {'term'; [NONT1, NONT2],.. }
		if tup[1][0] == "'" or tup[1][0] == '"':
			if tup[1] in self.terminals:
				if tup[0] not in self.terminals[tup[1]]:
					self.terminals[tup[1]].append(tup[0])
			else:
				self.terminals[tup[1]] = [tup[0]]

		else:
			if tup[1] in self.lhs:
				if tup[0] not in self.lhs[tup[1]]:
					self.lhs[tup[1]].append(tup[0])
			else:
				self.lhs[tup[1]] = [tup[0]]


	def getProbs(self):
	# probability of each production
		for key in self.rules:
			total = self.probFromFreq(key)
			for value in self.rules[key]:
				value[1] = value[1] / total


	def probFromFreq(self, key):
	# frequency of the lhs is the total of the counts of its rhs
		keyFrequency = 0
		for val in self.rules[key]:
			keyFrequency += val[1]

		return keyFrequency


	def buildPCFG(self):
	# prepare to output the grammar
		strBuilder = ''
		self.getProbs()
		for key in self.rules:
#			print self.rules[key]
			for value in sorted(self.rules[key]):
#				print value
				strBuilder = strBuilder + key + " -> " + value[0] + " [" + str(value[1]) + "]" + "\n"
		return strBuilder


	def getDS(self):
	# get the filled out data structures to pass them on to pcky
		return (self.rules, self.lhs, self.terminals)
		
