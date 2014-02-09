# Mike Roylance - roylance@uw.edu
import nltk.featstruct

def getFeature(featureProduction, fType):
	for (key, value) in featureProduction.viewitems():
		if str(key) == fType:
			return value
	return None

def getPos(featureProduction):
	return getFeature(featureProduction, "*type*")

def getNum(featureProduction):
	return getFeature(featureProduction, "NUM")

def getTerminal(tree):
	if len(tree) == 1:
		return tree[0]
	return None