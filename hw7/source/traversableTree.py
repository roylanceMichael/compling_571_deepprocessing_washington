import nltk

class TraversableTree:
	def __init__(self, tree, parent):
		self.tree = tree
		self.parent = parent
		self.children = []

		self.processChildren()

	def processChildren(self):
		for child in self.tree:
			# only want to process other tree
			if isinstance(child, nltk.Tree):
				newChild = TraversableTree(child, self.tree)
				self.children.append(newChild)