class Node():
	name = ""
	view_shape = "ellipse"

	def __init__(self, name):
		if ".py" in name:
			self.view_shape = "box"
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

	def view_to_graph(self):
		output = "	\"" + self.name + "\" [shape=" + self.view_shape + "]\n"
		output += "	\"" + self.name + "\" -> {"
		for link in self.links:
			output += link.name + " "
		output += "}\n"
		return output


