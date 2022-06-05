class Node():
	name = ""
	definition = ""

	def __init__(self, name):
		self.name = name
		self.links = list() # не нужно делать множестовм ссылки. Массивом будет проще удалять и сложнее объединять
		self.revert_links = list()

	def create_link(self, node):
		self.links.append(node)
		node.revert_links.append(self)

	def create_revert_link(self, node):
		node.revert_links.append(self)

	def __repr__(self):
		return repr(self.name)

	def __eq__(self, name_node):
		# print(name_node)
		if self.name == name_node:
			return True
		else:
			return False
