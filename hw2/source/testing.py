import nltk

def printWorkspace(workspace):
	for item in workspace:
		print item

def getAcceptableTuples(workspace, index):
	pass

# if we want to be CNF, we need to
# make sure if the length of RHS is 1, that it is a non-terminal

testGrammar = """
S -> NP VP

VP -> VP PP
VP -> V NP
VP -> 'eats'

PP -> P NP

NP -> Det N
NP -> 'she'

V -> 'eats'

P -> 'with'

N -> 'fish'
N -> 'fork'

Det -> 'a'
"""

chomskyGrammar = nltk.parse_cfg(testGrammar)

productions = chomskyGrammar.productions()

testInput = ['she', 'eats', 'a', 'fish', 'with', 'a', 'fork']

testInputLen = len(testInput)

workspace = []

# construct a triangular table
for i in range(0, testInputLen):
	subArray = []

	for j in range(0, testInputLen - i + 1):
		subArray.append([])

	workspace.append(subArray)

# let's set the initial level
for i in range(0, testInputLen):
	j = 0

	for production in productions:

		lhs = str(production.lhs())
		rhs = production.rhs()

		if len(rhs) == 1 and str(rhs[0]) == testInput[i]:
			workspace[i][j].append(lhs)

# print it out now
printWorkspace(workspace)

print '---'

for rowIndex in range(1, testInputLen):
	
	for i in range(0, testInputLen):

		if rowIndex >= len(workspace[i]):
			continue

		# I want to check behind me
		previousItems = {}

		for j in range(0, rowIndex):

			for item in workspace[i][j]:
				previousItems[item] = None

		nextIndex = i + 1
		if nextIndex >= testInputLen:
			continue

		nextItems = {}

		for j in range(0, rowIndex):

			for item in workspace[nextIndex][j]:

				nextItems[item] = None

		for production in productions:

			rhs = production.rhs()

			if len(rhs) == 2:

				lhs = str(production.lhs())
				rhs1 = str(rhs[0])
				rhs2 = str(rhs[1])

				for prevItem in previousItems:

					for nextItem in nextItems:

						if str(prevItem) == rhs1 and str(nextItem) == rhs2:
							workspace[i][rowIndex].append(lhs)

printWorkspace(workspace)






