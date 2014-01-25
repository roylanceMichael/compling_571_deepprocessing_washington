import nltk

# if we want to be CNF, we need to
# make sure if the length of RHS is 1, that it is a non-terminal
# 

grammarStr = """
A -> B T
A -> T C
C -> R X
C -> 'r'
R -> 'r'
X -> 'x'
B -> 'c'
T -> 't'
"""

grammar =  nltk.parse_cfg(grammarStr)
prods = grammar.productions()

print 'productions lexical'
for i in range(0, len(prods)):

	rhs = prods[i].rhs()
	print '--- non-terminals and is_lexical'
	print prods[i]

	print prods[i].is_lexical()
	for j in range(0, len(rhs)):
		print nltk.grammar.is_nonterminal(rhs[j])

	print '-- end non-terminals --'

print 'fin'
print grammar.is_flexible_chomsky_normal_form()
print grammar.is_chomsky_normal_form()