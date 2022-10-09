from class_node import Node
import re
import os
import subprocess
import json

path_json = os.getcwd() + "/json/local/"

def get_input_words():

	while 1:
		input_str = input("Ввод: ")
		if input_str == "":
			print("Введена пустая строка")
			continue

		input_str = input_str.lower()

		punctuation = '!"#$%&\'()*,-/;<=>@[\\]^`{|}~'
		for p in punctuation:
			if p in input_str:
				input_str = input_str.replace(p, '')

		input_list_words = input_str.split(" ")
		
		input_list_words = [ i for i in input_list_words if i]

		if input_list_words:
			return input_list_words
		else:
			print("Строка не содержит ни одного ключевого слова")


def run_nodes(input_list_words):

	output = ""

	json_files = os.listdir(path_json)

	path_python = os.getcwd() + "/python_programm"

	for i, word in enumerate(input_list_words):

		for file in json_files:
			if word == file[:-5]:
				with open(path_json + file) as json_file:
					data = json.load(json_file)

					# !!! если нет питона то не выполняем, а так все слова в предложении выполняются
					if "file" in data: 
						list_without_run_word = input_list_words.copy()
						list_without_run_word.remove(word)

						output = subprocess.check_output(["python3", path_python + "/" + data["file"]] + list_without_run_word, encoding='utf-8')

						if output:
							output = output.replace("\n", "")
							outout_list_words = []
							outout_list_words.append("сохрани_узлы")
							outout_list_words += output.split(" ")
							outout_list_words.append(word)
							run_nodes(outout_list_words)

	return output





def draw_graphviz():
	file_name = "graphs/local_graph.dot"
	with open(file_name, 'w') as f:
		f.write("strict graph G {\n")

		files_json = os.listdir(path_json)

		for file in files_json:
			with open(path_json + file) as json_file:
				data = json.load(json_file)

				if "link" in data:
					for link in data["link"]:
						
						if link == data["name"]:
							continue

						f.write(data["name"] + " -- " + link + "\n")

		f.write("}\n")


def write_to_local_graph(input_list_words):
	file_name = "graphs/local_graph.dot"
	with open(file_name, 'w') as f:
		f.write("strict graph G {\n")

		for word in input_list_words:
			for word_next in input_list_words:

				if word == word_next:
					continue

				# нужно дозаписывать в старый файл
				# если он нулевой, создавать верх и низ
				# в начале работы удалять


				f.write(word + " -- " + word_next + "\n")


		f.write("}\n")


if __name__ == "__main__":

	f = open('graphs/local_graph.json', 'w')
	f.close()

	f = open('output.json', 'w')
	f.close()

	while 1:

		input_list_words = get_input_words()

		write_to_local_graph(input_list_words)

		# output = run_nodes(input_list_words)

		# print("Вывод:", output)

		# # draw_graphviz()

		# f = open('output.json', 'w')
		# f.close()






	# очистка локального графа +

	# бесконечный цикл +

	# 	преобразование входных слов в  список понятий +
	# 	запись связей между понятиями в предложении в локальный граф
	# 	выполнение поочередно каждого слова в предложении с сохранением результата в общий файл
	# 		при наличии ответа создание новых узлов и связей
	# 		при рекурсивной зависимости выполнение других узлов внутри определения



















		#############################

		# версия 2

		# if "создай новое определение первого рода: " in input_str:
		# 	# definition_mode = True
		# 	input_str = input_str[39:] # 39, пототому что команда константой задана

		# 	input_list_words = input_str.split(" ")

		# 	# сейчас работает только один шаблон "слово file.py"
		# 	defenition = {}
		# 	defenition_name = input_list_words[0]
		# 	defenition['name'] = defenition_name
		# 	defenition['file'] = input_list_words[1]

		# 	with open("json/" + defenition_name + ".json", 'w') as outfile:
		# 		json.dump(defenition, outfile, ensure_ascii=False)

		# # подумать над выполнением команды "сохрани время"
		# # сохрани тоже превородное, вопрос в том, как папраметры передаются
		

		# if "дай определение: " in input_str:
		# 	# question_mode = False
		# 	input_str = input_str[17:]
			
		# 	input_list_words = input_str.split(" ")

		# 	path = os.getcwd() + "/json"
		# 	files = os.listdir(path)
		# 	for file in files:
		# 		if input_list_words[0] == file[:-5]:
		# 			with open("json/" + file) as json_file:
		# 				data = json.load(json_file)
						
		# 				path = os.getcwd() + "/python_programm"
		# 				output = subprocess.check_output(["python3", path + "/" + data["file"]])
		# 				output = str(output)[2:-3]

		# 				print("Вывод: " + output)

		# input_list_words = input_str.split(" ")

		# input_list_words = [ i for i in input_list_words if i]

		# input_list_nodes = convert_words_to_nodes(input_list_words)

		########################
		# версия 1

		# if question_mode:
			# pass
			# run_programm(input_list_nodes, graph_list_nodes)
			# run_node(input_list_nodes, graph_list_nodes)
			# read_node_to_graph(input_list_nodes, graph_list_nodes)
		# else:
			# graph_list_nodes = add_node_to_graph(input_list_nodes, graph_list_nodes)
			# graph_list_nodes = delete_node_to_graph(input_list_nodes, graph_list_nodes)

			# write_to_graph(graph_list_nodes, file_name)

