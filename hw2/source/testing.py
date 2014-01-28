import nltk

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

for val in testInput:
	for production in productions:
		rhs = production.rhs()

		if len(rhs) == 1 and str(rhs[0]) == val:
			print 'found ' + val


