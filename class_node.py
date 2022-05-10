class Node():
	name = ""

	def __init__(self, name):
		self.name = name
		self.links = []

	def create_link(self, node):
		self.links.append(node)

	def __repr__(self):
		return repr(self.name)

