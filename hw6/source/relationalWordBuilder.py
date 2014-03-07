import nltk
from nltk.corpus import wordnet as wn
import re

newLine = '\n'
noun = 'n'
comma = ','
whiteSpaces = '\s+'
emptyString = ''

class RelationalWordBuilder:
	def __init__(self, wsdContextsLocation):
		self.wsdContextsLocation = wsdContextsLocation
		self.allWords = {}
		self.generateAllWords()

	def getAllWords(self):
		for word in self.allWords:
			yield word

	def generateAllWords(self):
		wsdContextsStream = open(self.wsdContextsLocation)
		wsdContextsLine = wsdContextsStream.readline()

		while wsdContextsLine:
			self.processLine(wsdContextsLine)
			wsdContextsLine = wsdContextsStream.readline()

	def processLine(self, line):
		splitLine = re.split(whiteSpaces, line)

		if len(splitLine) < 1:
			return

		word = splitLine[0]
		self.setWord(word)

		contexts = re.split(comma, splitLine[1])
		for context in contexts:
			self.setWord(context)

	def setWord(self, word):
		wordSenses = wn.synsets(word)

		for wordSense in wordSenses:
			
			if wordSense.pos != 'n':
				continue

			for lemma in wordSense.lemmas:
				self.allWords[lemma.name] = None