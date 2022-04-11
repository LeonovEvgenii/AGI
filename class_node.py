class Node():
	name = ""

	def __init__(self, name):
		self.name = name
		self.links = []

	def create_link(self, node):
		print("create_link")
		# self.links = [node]
		self.links.append(node)


# stol = Node("стол")

# print(stol.name)

# stul = Node("стол")
# pol = Node("пол", [stol, stul])

# print(stol.name)

