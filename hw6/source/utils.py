from collections import defaultdict

# http://nltk.googlecode.com/svn-hist/trunk/doc/api/nltk.corpus.reader.wordnet-pysrc.html#WordNetICCorpusReader.ic - thank you!
def buildIc(icFile):
	ic = {} 
	
	NOUN = 'n'
	VERB = 'v'

	ic[NOUN] = defaultdict(float) 
	ic[VERB] = defaultdict(float) 
	
	for num, line in enumerate(open(icFile)): 
		if num == 0: # skip the header 
			continue 
		
		fields = line.split() 
		offset = int(fields[0][:-1]) 
		value = float(fields[1]) 
		# only dealing with nouns
		pos = NOUN
		
		if len(fields) == 3 and fields[2] == "ROOT": 
			# Store root count. 
			ic[pos][0] += value 
		if value != 0: 
			ic[pos][offset] = value 
	
	return ic 