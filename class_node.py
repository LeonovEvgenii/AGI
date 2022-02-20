class Node():
	name = ""
	bind = []

	def __init__(self, name, binds=None):
		self.name = name

		if binds:
			for i in binds:
				self.bind.append(i)


stol = Node("стол")

# print(stol.name)

stul = Node("стол")
pol = Node("пол", [stol, stul])

print(pol.bind)