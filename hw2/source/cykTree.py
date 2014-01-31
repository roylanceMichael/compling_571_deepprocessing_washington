import nltk
import cky
import copy

def isPairInGrammar(pair, productions):
	for production in productions:
		rhs = production.rhs()

		if len(rhs) == 2:
			if str(pair[0]) == str(rhs[0]) and str(pair[1]) and str(rhs[1]):
				return True

	return False

def addToMultiArray(vals, itemToAdd):
	if type(vals[0]) == type([]):
		for val in vals:
			val.append(itemToAdd)
	else:
		vals.append(itemToAdd)

def recursiveBuildParse(vals, workspace, rowIndex, level, productions, sentence):
	if level == 0:
		addToMultiArray(vals, sentence[rowIndex])

	for i in range(0, level):
		firstComparison = (rowIndex, level - i - 1)
		secondComparison = (rowIndex + level - i, i)

		firstItems = workspace[firstComparison[0]][firstComparison[1]]

		if (secondComparison[0] < len(workspace) and 
			secondComparison[1] < len(workspace[secondComparison[0]])):

			secondItems = workspace[secondComparison[0]][secondComparison[1]]

			totalNum = 0
			for firstItem in firstItems:
				for secondItem in secondItems:
					if isPairInGrammar((firstItem, secondItem), productions):
						totalNum = totalNum + 1

						if totalNum > 1:
							continue

						firstItemVals = [firstItem]
						recursiveBuildParse(firstItemVals, workspace, firstComparison[0], firstComparison[1], productions, sentence)
						
						secondItemVals = [secondItem]
						recursiveBuildParse(secondItemVals, workspace, secondComparison[0], secondComparison[1], productions, sentence)

						if totalNum > 1:
							vals[len(vals)-1].append(firstItemVals)
							vals[len(vals)-1].append(secondItemVals)
						else:
							addToMultiArray(vals, firstItemVals)
							addToMultiArray(vals, secondItemVals)
						
def getParseTree(workspace, productions, sentence):
	topNodeLen = len(workspace[0])

	topNodes = workspace[0][topNodeLen-1]

	for topNode in topNodes:
		reference = [[topNode]]
		recursiveBuildParse(reference, workspace, 0, topNodeLen-1, productions, sentence)
		return reference