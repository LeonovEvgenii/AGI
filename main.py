from class_node import Node
import re


def write_to_graph(list_nodes):
	with open("graph.dot", 'w') as f:
		f.write("digraph G {\n")
		for node in list_nodes:
			f.write("  \"" + node.name + "\";\n")
			if len(node.links) > 0:
				for link in node.links:
					f.write("  \"" + node.name + "\" -> \"" + link.name + "\";\n")
		f.write("}\n")

def clear_graph():
	with open("graph.dot", 'w') as f:
		f.write("digraph G {\n\n")
		f.write("}\n")

def get_obj_graph():
	with open("graph.dot", 'r') as f:
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

			# если нужно ссылку добавить, то и в новом элементе обратную ссылку делаем
			# в функции обратной ссылки можно и прямую делать и абзац выше убать с ручным сравнением

			# позже проверть как удалятся элементы, которые друг на друга ссылаются, должен остаться один, который не удаляется	
		
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

if __name__ == "__main__":

	clear_graph()

	while 1:
		graph_list_nodes = get_obj_graph()
		input_str = input("Введи факт: ")
		if input_str == "":
			print("Введена пустая строка")
			continue
		input_list_words = input_str.split(" ")

		input_list_nodes = convert_words_to_nodes(input_list_words)

		graph_list_nodes = add_node_to_graph(input_list_nodes, graph_list_nodes)
		# graph_list_nodes = delete_node_to_graph(input_list_nodes, graph_list_nodes)

		write_to_graph(graph_list_nodes)





