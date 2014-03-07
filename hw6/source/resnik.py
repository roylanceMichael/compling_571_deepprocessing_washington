
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

		for context in contexts:

			misValue = 0
			maxWordSynset = None
			maxContextSynset = None
			mostInformativeSubsumer = None

			contextSynsets = wn.synsets(context)

			# get the MIS
			for wordSynset in wordSynsets:
				for contextSynset in contextSynsets:
					(value, subsumer) = self.reznik(wordSynset, contextSynset)

					if value > misValue:
						misValue = value
						mostInformativeSubsumer = subsumer
						maxWordSynset = wordSynset
						maxContextSynset = contextSynset

			# handle the case when we don't have an MIS
			if mostInformativeSubsumer is None:
				yield '(' + word + ', ' + context + ', ' + str(0) + ') '
				continue
			else:
				yield '(' + word + ', ' + context + ', ' + str(misValue) + ') '

			# set the score
			if maxWordSynset in scores:
				scores[maxWordSynset] = scores[maxWordSynset] + misValue
			else:
				scores[maxWordSynset] = misValue

		maxScore = 0
		maxSynset = None

		# select the best sense for the word
		for wordSynset in scores:
			if scores[wordSynset] > maxScore:
				maxScore = scores[wordSynset]
				maxSynset = wordSynset

		yield newLine
		yield maxSynset.name
		yield newLine

	# resnik similarity
	def reznik(self, wordSynset, contextSynset):
		if wordSynset.pos != noun:
			return (0, None)

		# get the hypernyms
		subsumers = wordSynset.common_hypernyms(contextSynset)
		maxValue = 0
		maxSubsumer = None

		# handle when 0
		if len(subsumers) == 0:
			return (maxValue, maxSubsumer)
		
		maxValue = 0
		maxSubsumer = None
		for subsumer in subsumers:

			if subsumer.pos != noun:
				continue
				
			result = nltk.corpus.reader.information_content(subsumer, self.ic)

			if result > maxValue:
				maxValue = result
				maxSubsumer = subsumer

		return (maxValue, maxSubsumer)






