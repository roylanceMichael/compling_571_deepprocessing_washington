import re
from nltk.corpus import wordnet as wn

# static variables
noun = 'n'
comma = ','
whiteSpaces = '\s+'
emptyString = ''

class Resnik
	# ic is nltk ic
	# wsdContexts is 
	def __init__(self, ic):
		self.ic = ic

	def processLine(self, line):
		splitLine = re.split(whiteSpaces, line)

		if len(splitLine) < 1:
			return emptyString

		word = splitLine[0]

		contexts = re.split(comma, splitLine[1])

		if len(contexts) == 0:
			return emptyString

		wordSynsets = wn.synset(word)

		# senses are synsets
		# therefore, we want to find the best synset for a word
		# we go through each word's synsets
		# and compare it to each context's synset
		# we get the hypernyms
		# the score with the highest wins overall

		for wordSynset in wordSynsets:

			# only handle nouns 'n'
			if wordSynset.pos != noun:
				continue

			for context in contexts:
				
				contextSynsets = wn.synset(context)

				for contextSynset in contextSynsets:

					reznikValue = self.reznik(wordSynset, contextSynset)

	def reznik(self, wordSynset, contextSynset):
		if wordSynset.pos != noun:
			return 0

		subsumers = wordSynset.common_hypernyms(contextSynset)

		# handle when 0
		if len(subsumers) == 0:
			return 0
		else:
			return max(nltk.corpus.reader.information_content(subsumer, self.ic) for subsumer in subsumers)






