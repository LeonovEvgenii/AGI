class Node():
	name = ""

	def __init__(self, name):
		self.name = name
		self.links = set()

	def create_link(self, node):
		self.links.add(node.name)

	def __repr__(self):
		return repr(self.name)

	def __eq__(self, name_node):
		# print(name_node)
		if self.name == name_node:
			return True
		else:
			return False
