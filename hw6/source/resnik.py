import re
import nltk
from nltk.corpus import wordnet as wn

# static variables
newLine = '\n'
noun = 'n'
comma = ','
whiteSpaces = '\s+'
emptyString = ''

class Resnik:
	# ic is nltk ic
	# wsdContexts is 
	def __init__(self, ic):
		self.ic = ic

	def processLine(self, line):
		splitLine = re.split(whiteSpaces, line)

		if len(splitLine) < 1:
			yield emptyString
			return

		word = splitLine[0]

		contexts = re.split(comma, splitLine[1])

		if len(contexts) == 0:
			yield emptyString
			return
		
		wordSynsets = wn.synsets(word)

		# senses are synsets
		# therefore, we want to find the best synset for a word
		# we go through each word's synsets
		# and compare it to each context's synset
		# we get the hypernyms
		# the score with the highest wins overall

		scores = {}

		for wordSynset in wordSynsets:

			# only handle nouns 'n'
			if wordSynset.pos != noun:
				continue

			scores[wordSynset] = {}

			for context in contexts:
				
				contextSynsets = wn.synsets(context)
				maxSynset = None
				maxValue = 0

				for contextSynset in contextSynsets:

					reznikValue = self.reznik(wordSynset, contextSynset)

					if reznikValue > maxValue:
						maxValue = reznikValue
						maxSynset = contextSynset

				scores[wordSynset][context] = maxValue

		# go through and print out the max ones 
		for context in contexts:
			maxScore = 0

			for wordSynset in scores:
				score = scores[wordSynset][context]
				if score > maxScore:
					maxScore = score

			strVal = '(' + word + ', ' + context + ', ' + str(maxScore) + ') '

			yield strVal

		maxScore = 0
		maxSynset = None

		for wordSynset in scores:
			tempMaxScore = 0

			for context in scores[wordSynset]:
				tempMaxScore = tempMaxScore + scores[wordSynset][context]

			if tempMaxScore > maxScore:
				maxScore = tempMaxScore
				maxSynset = wordSynset

		yield newLine
		yield maxSynset.name
		yield newLine

	def reznik(self, wordSynset, contextSynset):
		if wordSynset.pos != noun:
			return 0

		subsumers = wordSynset.common_hypernyms(contextSynset)

		# handle when 0
		if len(subsumers) == 0:
			return 0
		else:
			return max(nltk.corpus.reader.information_content(subsumer, self.ic) for subsumer in subsumers)






