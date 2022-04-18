class Node():
	name = ""

	def __init__(self, name):
		self.name = name
		self.links = []

	def create_link(self, node):
		self.links.append(node)



