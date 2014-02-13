# Mike Roylance - roylance@uw.edu
import nltk.featstruct

# get specific information about a grammar feature
def getFeature(featureProduction, fType):
	for (key, value) in featureProduction.viewitems():
		if str(key) == fType:
			return value
	return None

# get the part of speech for a feature
def getPos(featureProduction):
	return getFeature(featureProduction, "*type*")

# get the num feature
def getNum(featureProduction):
	return getFeature(featureProduction, "NUM")

# get the tense feature
def getTense(featureProduction):
	return getFeature(featureProduction, "TENSE")

# determine if it's a terminal, if it is return it. if not, return nothing
def getTerminal(tree):
	if len(tree) == 1:
		return tree[0]
	return None