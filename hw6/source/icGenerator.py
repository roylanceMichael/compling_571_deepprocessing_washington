# Mike Roylance - roylance@uw.edu
import os
import sys
import re
import math
from nltk.corpus import wordnet as wn

whiteSpace = "\s+"
forwardSlash = "/"

class IcGenerator:
	def __init__(self, words, brownCorpusLocation, icFileLocation):
		self.icFileLocation = icFileLocation

		self.words = {}

		for word in words:
			self.words[word] = 1

		self.pos = {}
		self.pos["nn"] = None
		self.pos["nn$"] = None
		self.pos["nns"] = None
		self.pos["nns$"] = None
		self.pos["np"] = None
		self.pos["np$"] = None
		self.pos["nps"] = None
		self.pos["nps$"] = None
		self.pos["nr"] = None
		self.pos["pn"] = None
		self.pos["pn$"] = None
		self.pos["pp$"] = None
		self.pos["pp$$"] = None
		self.pos["ppl"] = None
		self.pos["ppls"] = None
		self.pos["ppo"] = None
		self.pos["pps"] = None
		self.pos["ppss"] = None
		self.pos["prp"] = None
		self.pos["prp$"] = None

		self.brownCorpusLocation = brownCorpusLocation
		self.totalWords = 0

	def generate(self):
		self.totalWords = 0
		
		# go to corpus
		for brownFile in os.listdir(self.brownCorpusLocation):

			brownFileStream = open(self.brownCorpusLocation + '/' + brownFile)
			brownFileLine = brownFileStream.readline()

			while brownFileLine:
				self.handleLine(brownFileLine)
				brownFileLine = brownFileStream.readline()

		# print new file
		# wnver::eOS9lXC6GvMWznF1wkZofDdtbBU
		with open(self.icFileLocation, 'w') as newIcFile:
			# not quite sure what this does
			newIcFile.write('wnver::eOS9lXC6GvMWznF1wkZofDdtbBU' + '\n')
			newIcFile.write('1740n ' + str(self.totalWords) + ' ROOT\n')
			self.handleFileWrite(newIcFile)

	def handleFileWrite(self, newIcFile):
		for word in self.words:
			synsets = wn.synsets(word)

			count = self.words[word]
			total = self.totalWords

			logProb = -math.log(float(count) / self.totalWords)

			for synset in synsets:
					line = str(synset.offset) + 'n' + ' ' + str(logProb) + '\n'
					newIcFile.write(line)

	def handleLine(self, line):
		# split by white space
		tokens = re.split(whiteSpace, line)

		for token in tokens:
			wordAndPos = re.split(forwardSlash, token)

			if len(wordAndPos) > 1:
				self.totalWords = self.totalWords + 1
				word = wordAndPos[0].strip()
				pos = wordAndPos[1].strip()

				# is our word in our dictionary?
				if word in self.words and pos in self.pos:
					self.words[word] = self.words[word] + 1