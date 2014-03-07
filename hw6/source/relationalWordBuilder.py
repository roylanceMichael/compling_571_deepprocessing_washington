# Mike Roylance - roylance@uw.edu
import nltk
from nltk.corpus import wordnet as wn
import re

newLine = '\n'
noun = 'n'
comma = ','
whiteSpaces = '\s+'
emptyString = ''

class RelationalWordBuilder:
	# ctor
	def __init__(self, wsdContextsLocation):
		self.wsdContextsLocation = wsdContextsLocation
		self.allWords = {}
		self.generateAllWords()

	# get all the words
	def getAllWords(self):
		for word in self.allWords:
			yield word

	# generate all words based on the wsdContexts file
	def generateAllWords(self):
		wsdContextsStream = open(self.wsdContextsLocation)
		wsdContextsLine = wsdContextsStream.readline()

		while wsdContextsLine:
			self.processLine(wsdContextsLine)
			wsdContextsLine = wsdContextsStream.readline()

	# process each line
	def processLine(self, line):
		splitLine = re.split(whiteSpaces, line)

		if len(splitLine) < 1:
			return

		word = splitLine[0]
		self.setWord(word)

		contexts = re.split(comma, splitLine[1])
		for context in contexts:
			self.setWord(context)

		# get all subsumers too
		for wordSense in wn.synsets(word):
			for context in contexts:
				for contextWordSense in wn.synsets(context):
					subsumers = wordSense.common_hypernyms(contextWordSense)

					for subsumer in subsumers:
						if subsumer.pos != 'n':
							for lemma in subsumer.lemmas:
								self.allWords[lemma.name] = None


	# get all the senses and lemmas associated with the word for use in the custom IC file
	def setWord(self, word):
		wordSenses = wn.synsets(word)

		for wordSense in wordSenses:
			
			if wordSense.pos != 'n':
				continue

			for lemma in wordSense.lemmas:
				self.allWords[lemma.name] = None