class ItemIndex:
	def __init__(self, item, pos, subTree, rootTree, index):
		self.item = item
		self.pos = pos
		self.subTree = subTree
		self.rootTree = rootTree
		self.index = index

	def __str__(self):
		return "%s %s %s %s" % (self.item, self.pos, self.index, self.subTree)