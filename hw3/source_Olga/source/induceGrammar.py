from __future__ import division
import nltk
import re


class InduceGrammar:
	def __init__(self):
		self.rules = {}
		self.lhs = {}
		self.terminals = {}


	def LHS_RHS(self, line):
		match = re.search(r'(\w+\'*)\s*(->|=>|>)(.+$)', line)
		if match:
			lhs = match.group(1)
			all_rhs = match.group(3)
		else:
			print 'match not found'

		all_rhs = all_rhs.strip()

		tup = (lhs, all_rhs)
#		print tup	
		return tup



	def fillDicts(self, line):
		tup = self.LHS_RHS(line)
#		print tup[0], tup[1]
		if tup[0] in self.rules:
			listofprod = []

			for prod in self.rules[tup[0]]:
				listofprod.append(prod[0])
			for prod in self.rules[tup[0]]:
				if tup[1] in prod[0]:
#					print 'found something!'
					prod[1] = prod[1] + 1
			if tup[1] not in listofprod:
				newProd = [tup[1], 1]
				self.rules[tup[0]].append(newProd)
		else:
			self.rules[tup[0]] = [[tup[1], 1]]
		
		self.getLHSAndTerminals(tup)
#		print self.lhs



	def getLHSAndTerminals(self, tup):
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
		for key in self.rules:
			total = self.probFromFreq(key)
			for value in self.rules[key]:
				value[1] = value[1] / total


	def probFromFreq(self, key):
		keyFrequency = 0
		for val in self.rules[key]:
			keyFrequency += val[1]

		return keyFrequency


	def buildPCFG(self):
		strBuilder = ''
		self.getProbs()
		for key in self.rules:
#			print self.rules[key]
			for value in sorted(self.rules[key]):
#				print value
				strBuilder = strBuilder + key + " -> " + value[0] + " [" + str(value[1]) + "]" + "\n"
		return strBuilder


	def getDS(self):
		return (self.rules, self.lhs, self.terminals)
		
