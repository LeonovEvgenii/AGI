import os
import json

path_json_local = os.getcwd() + "/json/local/"

def write_to_local_graph_json(input_list_words):

	# сейчас образуются пары слов
	# альтернатива сделать связи все со всеми

	# запись идет во внутрениний формат, т к xdot ограничен

	input_pairs = []
	for index, word in enumerate(input_list_words):
		input_pair = []
		input_pair.append(word)
		try:
			input_pair.append(input_list_words[index + 1])
			input_pairs.append(input_pair)
		except IndexError:
			break

	# добавить сортировку input_pairs

	if os.stat("graphs/local_graph.json").st_size != 0:
		save_pairs = None
		with open("graphs/local_graph.json") as json_file:
			save_pairs = json.load(json_file)

			for input_pair in input_pairs:
				if input_pair in save_pairs or [input_pair[1], input_pair[0]] in save_pairs:
					continue
				else:
					save_pairs.append(input_pair)

		with open("graphs/local_graph.json", 'w') as outfile:
			json.dump(save_pairs, outfile, ensure_ascii=False)

	else:
		# использую список списков т к множества json не поддерживает

		with open("graphs/local_graph.json", 'w') as outfile:
			json.dump(input_pairs, outfile, ensure_ascii=False)


def print_to_xdot_local():

	save_pairs = None
	with open("graphs/local_graph.json") as json_file:
		save_pairs = json.load(json_file)

	file_name = "graphs/local_graph.dot"
	with open(file_name, 'w') as f:
		f.write("strict graph G {\n")

		for save_pair in save_pairs:
			f.write('"' + save_pair[0] + '" -- "' + save_pair[1] + '"\n')

		f.write("}\n")

def print_to_xdot_global():

	save_pairs = None
	with open("graphs/global_graph.json") as json_file:
		save_pairs = json.load(json_file)

	file_name = "graphs/global_graph.dot"
	with open(file_name, 'w') as f:
		f.write("strict graph G {\n")

		for save_pair in save_pairs:
			f.write('"' + save_pair[0] + '" -- "' + save_pair[1] + '"\n')

		f.write("}\n")


def clear_local_graph():

	print("\nочищаю локальный граф\n")

	f = open('graphs/local_graph.json', 'w')

	with open('graphs/local_graph.dot', 'w') as f:
		f.write("strict graph G {\n")
		f.write("}\n")
	f.close()

	f = open('output.json', 'w')
	f.close()

	try:
		local_files = os.listdir(path_json_local)
	except FileNotFoundError:
		return

	if local_files:
		os.system("rm " + path_json_local + "*")