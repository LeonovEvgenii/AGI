import os
import json
import time

from scripts.classes._Class import _Class
from scripts.classes._Object import _Object


path_json_local = os.getcwd() + "/json/local/"

def proseccing_input_words(input_str):
	input_str = input_str.lower()

	punctuation = '!"#$%&\'()*,;@[\\]^`{|}~'
	for p in punctuation:
		if p in input_str:
			input_str = input_str.replace(p, '')

	input_list_words = input_str.split(" ")
	
	input_list_words = [ i for i in input_list_words if i ]

	return input_list_words


def get_input_objects_and_classes(local_list_objects, local_list_classes):

	while 1:
		input_str = input("Ввод: ")
		if input_str == "":
			print("Введена пустая строка")
			continue

		input_list_words = proseccing_input_words(input_str)

		input_list_objects = []
		input_list_classes = []

		if input_list_words:

			for i, word in enumerate(input_list_words):
				
				class_in_list = False

				for _class in local_list_classes:
					if _class.name == word:
						new_object = _Object(_class, i + 1)
						input_list_objects.append(_Object(_class, i + 1))
						local_list_objects.append(_Object(_class, i + 1))

						_class.list_objects.append(new_object)
						class_in_list = True
					
				# Проверки на уже существование класса осуществляются только для локального графа.
				# Во время выполненения нод может быть косяк, когда сначала поиск идет по локальному графу
				# потом по глобальному. В слове из локального графа может не оказаться определения.
				# Но логично, что сначала смотрим на локальный граф, т к это последний контекст.
				# Сейчас переход в глобальный осуществляется только по команде в ручном режиме.

				if not class_in_list:
					new_class = _Class(word)
					input_list_classes.append(new_class)
					local_list_classes.append(new_class)

					new_object = _Object(new_class, i + 1)
					input_list_objects.append(new_object)
					local_list_objects.append(new_object)

					new_class.list_objects.append(new_object)

			return input_list_objects, input_list_classes
		else:
			print("Строка не содержит ни одного ключевого слова")


def write_to_local_graph_json(input_list_words):

	# сейчас образуются пары слов
	# альтернатива сделать связи все со всеми

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


def write_local_links(input_list_objects, local_list_links):

	count_obj = len(input_list_objects)
	for index, obj in enumerate(input_list_objects):
		
		input_pair = set()
		
		if index % 2 == 0:
			if index + 1 == count_obj:
				input_pair.add(obj)
				# проверка на существование элемнта не нужна
				# т к из за разного времени ввода экземпляры класса объект всегда будут разные
				# даже если делать проверку, то через оператор in, а не через set
				local_list_links.append(input_pair)
			else:
				input_pair.add(obj)
				input_pair.add(input_list_objects[index + 1])
				local_list_links.append(input_pair)
		else:
			continue

	# теперь нужно добавить связь ноды объекта с нодой класса
	# по хорошему надо сделать класс нода, от которого наследуются класс класс и обект
	# отрисовка переопределяется в каждом
	# будут ли бругие типы нод, например датчик?

	# отрисовка пар
	# for i in local_list_links:
	# 	print("пара")
	# 	for j in i:
	# 		print(j.class_name)



def print_to_xdot_local(local_list_classes):

	# Источником связей могут служить список и файл json
	# Приоритетный источник список
	# Файл позже продублируется

	file_name = "knowledge_base/graphs_links/local_graph.dot"
	with open(file_name, 'w') as f:
		f.write("strict graph G {\n")

		for _class in local_list_classes:
			for i, obj in enumerate(_class.list_objects):
				f.write('"' + obj.class_name + '\n' + str(i + 1) + '"\n')

		f.write("}\n")

	# Старый код чтения из json

	# input_json = None
	# with open("graphs/local_graph.json") as json_file:
	# 	input_json = json.load(json_file)

	# file_name = "graphs/local_graph.dot"
	# with open(file_name, 'w') as f:
	# 	f.write("strict graph G {\n")

	# 	for node in input_json['nodes']:
	# 		f.write('"' + node + '"\n')

	# 	for save_pair in input_json['links']:
	# 		if len(save_pair) == 2: 
	# 			f.write('"' + save_pair[0] + '" -- "' + save_pair[1] + '"\n')
	# 		else:
	# 			f.write('"' + save_pair[0] + '"\n')

	# 	f.write("}\n")




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
