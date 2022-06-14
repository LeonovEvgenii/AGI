from class_node import Node
import re


def write_to_graph(list_nodes, file_name):
	with open(file_name, 'w') as f:
		f.write("digraph G {\n")
		for node in list_nodes:
			f.write("  \"" + node.name + "\";\n")
			if len(node.links) > 0:
				for link in node.links:
					f.write("  \"" + node.name + "\" -> \"" + link.name + "\";\n")
		f.write("}\n")

def clear_graph(file_name):
	with open(file_name, 'w') as f:
		f.write("digraph G {\n\n")
		f.write("}\n")

def get_obj_graph(file_name):
	with open(file_name, 'r') as f:
		lines = f.readlines()

		elements = set()
		links = set()
		elements_link = set()
		for line in lines[1:-1]:
			l = re.sub(" |;|\n|\"", "", line)
			if l == '':
				continue
			l = l.split("->")
			if len(l) > 1:
				links.add((l[0], l[1]))
				elements_link.add(l[0])
				elements_link.add(l[1])
			
			for _ in l:
				elements.add(_)

	graph_list_nodes = []
	for element in elements:
		graph_list_nodes.append(Node(element))

	# добавляю ссылки в список нод
	for link in links:
		for node in graph_list_nodes:
			if node.name == link[0]:
				for node_2 in graph_list_nodes:
					if node_2.name == link[1]:
						node.create_link(node_2)

	if len(graph_list_nodes) == 0:
		print("Граф был пустым")

	return graph_list_nodes

def convert_words_to_nodes(input_list_words):
	input_list_nodes = []

	if len(input_list_words) == 1:
		input_list_nodes.append(Node(input_list_words[0]))
	else:
		for i, word in enumerate(input_list_words):
			node = Node(word)
		
			try:
				node_2 = Node(input_list_words[i+1])
				node.create_link(node_2)
				input_list_nodes.append(node)
			except IndexError:
				input_list_nodes.append(node)
		
	return input_list_nodes


def add_node_to_graph(input_list_nodes, graph_list_nodes):
	
	for node_input in input_list_nodes:

		if len(graph_list_nodes) > 0:

			number_compare_node = None

			for i, node_graph in enumerate(graph_list_nodes):
				if node_input == node_graph:
					number_compare_node = i
					break

			if number_compare_node == None:
				graph_list_nodes.append(node_input)
			else:
				for link_input in node_input.links:
					if link_input not in graph_list_nodes[number_compare_node].links:
						graph_list_nodes[number_compare_node].links.append(link_input)
						link_input.create_revert_link(graph_list_nodes[number_compare_node])
		
		else:
			graph_list_nodes.append(node_input)
		
	return graph_list_nodes


def delete_node_to_graph(input_list_nodes, graph_list_nodes):

	for node_input in input_list_nodes:

		if len(graph_list_nodes) > 0:

			for node_graph in graph_list_nodes:
				if node_input == node_graph:

					for revert_link in node_graph.revert_links:
						revert_link.links.remove(node_input)

					graph_list_nodes.remove(node_graph)
					break

		else:
			break
		
	return graph_list_nodes

def read_node_to_graph(input_list_nodes, graph_list_nodes, i = 0):
	if i > 5:
		return
	
	print(i)
	input_node = input_list_nodes[0]
	
	for node_graph in graph_list_nodes:
		if input_node == node_graph:
			print(node_graph.links)

			for link in node_graph.links:
				i += 1
				read_node_to_graph([link], graph_list_nodes, i)

			# print(node_graph.revert_links)


if __name__ == "__main__":

	file_name = "local_graph.dot"
	# clear_graph(file_name)

	# file_name = "global_graph.dot"

	while 1:
		question = False

		graph_list_nodes = get_obj_graph(file_name)
		input_str = input("Введи факт: ")
		if input_str == "":
			print("Введена пустая строка")
			continue

		input_str = input_str.lower()

		punctuation = '!"#$%&\'()*,-./:;<=>@[\\]^_`{|}~'
		for p in punctuation:
			if p in input_str:
				input_str = input_str.replace(p, '')

		if input_str[-1] == "?":
			question = True
			input_str = input_str[:-1]

		input_list_words = input_str.split(" ")

		input_list_words = [ i for i in input_list_words if i]

		input_list_nodes = convert_words_to_nodes(input_list_words)

		if question:
			pass
			# read_node_to_graph(input_list_nodes, graph_list_nodes)
		else:
			graph_list_nodes = add_node_to_graph(input_list_nodes, graph_list_nodes)
			# graph_list_nodes = delete_node_to_graph(input_list_nodes, graph_list_nodes)

			write_to_graph(graph_list_nodes, file_name)

