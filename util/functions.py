import os
import json
import time

path_json_local = os.getcwd() + "/json/local/"

def proseccing_input_words(input_str):
	input_str = input_str.lower()

	punctuation = '!"#$%&\'()*,;@[\\]^`{|}~'
	for p in punctuation:
		if p in input_str:
			input_str = input_str.replace(p, '')

	input_list_words = input_str.split(" ")
	
	input_list_words = [ i for i in input_list_words if i ]
	
	second = int(time.time())

	divider = 1 / len(input_list_words)

	input_list_words = [ word + "$" + str(second + divider * i) for i, word in enumerate(input_list_words) ]

	return input_list_words


def get_input_words():

	while 1:
		input_str = input("Ввод: ")
		if input_str == "":
			print("Введена пустая строка")
			continue

		input_list_words = proseccing_input_words(input_str)

		if input_list_words:
			return input_list_words
		else:
			print("Строка не содержит ни одного ключевого слова")


def write_to_local_graph_json(input_list_words):

	# сейчас образуются пары слов
	# альтернатива сделать связи все со всеми

	# запись идет во внутрениний формат, т к xdot ограничен

	# формирование списка пар из входных слов
	input_pairs = []
	for index, word in enumerate(input_list_words):
		input_pair = []
		input_pair.append(word)
		try:
			input_pair.append(input_list_words[index + 1])
			input_pairs.append(input_pair)
		except IndexError:
			if len(input_list_words) == 1:
				input_pairs.append(input_pair)
			break

	# добавить сортировку input_pairs # зачем?
	# зачем я в файле графа в json в ключе links пишу ноды, у которых нет связей?

	# добавление новых пар в список уже существующих
	if os.stat("graphs/local_graph.json").st_size != 0:
		out_json = None
		with open("graphs/local_graph.json") as json_file:
			out_json = json.load(json_file)

			# добавлеие названий узлов, удаление копий
			out_json['nodes'] = list(set((out_json['nodes'] + input_list_words)))

			# добавлеие связей
			for input_pair in input_pairs:
				if len(input_pair) == 2:
					if input_pair in out_json['links'] or [input_pair[1], input_pair[0]] in out_json['links']:
						continue
					else:
						out_json['links'].append(input_pair)
				else:
					if input_pair in out_json['links']:
						continue
					else:
						out_json['links'].append(input_pair)

		with open("graphs/local_graph.json", 'w') as outfile:
			json.dump(out_json, outfile, ensure_ascii=False)

	else:
		# использую список списков т к множества json не поддерживает

		out_json = {}
		out_json['nodes'] = input_list_words
		out_json['links'] = input_pairs

		with open("graphs/local_graph.json", 'w') as outfile:
			json.dump(out_json, outfile, ensure_ascii=False)


def print_to_xdot_local():

	input_json = None
	with open("graphs/local_graph.json") as json_file:
		input_json = json.load(json_file)

	file_name = "graphs/local_graph.dot"
	with open(file_name, 'w') as f:
		f.write("strict graph G {\n")

		for node in input_json['nodes']:
			f.write('"' + node + '"\n')

		for save_pair in input_json['links']:
			if len(save_pair) == 2: 
				f.write('"' + save_pair[0] + '" -- "' + save_pair[1] + '"\n')
			else:
				f.write('"' + save_pair[0] + '"\n')

		f.write("}\n")


def print_to_xdot_global():

	input_json = None
	with open("graphs/global_graph.json") as json_file:
		input_json = json.load(json_file)

	file_name = "graphs/global_graph.dot"
	with open(file_name, 'w') as f:
		f.write("strict graph G {\n")

		for node in input_json['nodes']:
			f.write('"' + node + '"\n')

		for save_pair in input_json['links']:
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


def save_new_nodes(input_list_words):

	files = os.listdir(path_json_local)
	for word in input_list_words:
		word_class = word[:word.rfind("$")]

		word_instance = word[word.rfind("$"):]

		path_file_class = "json/local/" + word_class + ".json"

		if not word_class + ".json" in files:
			defenition = {}
			defenition['name'] = word_class
			defenition['instances'] = []
			defenition['instances'].append(word_instance)
			with open(path_file_class, 'w') as outfile:
				json.dump(defenition, outfile, ensure_ascii=False)
			outfile.close()
		else:

			defenition = None
			with open(path_file_class) as json_file:
				defenition = json.load(json_file)

			defenition["instances"].append(word_instance)

			file_name = path_file_class
			with open(file_name, 'w') as json_file:
				json.dump(defenition, json_file, ensure_ascii=False)
