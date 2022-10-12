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


def write_to_local_graph_json(input_list_words):

	# print("входные слова", input_list_words)

	input_pairs = []
	for index, word in enumerate(input_list_words):
		input_pair = []
		input_pair.append(word)
		try:
			input_pair.append(input_list_words[index + 1])
			input_pairs.append(input_pair)
		except IndexError:
			break

	# print("образованные пары", input_pairs)

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

			


def print_to_xdot():

	save_pairs = None
	with open("graphs/local_graph.json") as json_file:
		save_pairs = json.load(json_file)

	file_name = "graphs/local_graph.dot"
	with open(file_name, 'w') as f:
		f.write("strict graph G {\n")

		for save_pair in save_pairs:
			f.write('"' + save_pair[0] + '" -- "' + save_pair[1] + '"\n')

		f.write("}\n")


if __name__ == "__main__":

	f = open('graphs/local_graph.json', 'w')
	f.close()

	f = open('output.json', 'w')
	f.close()

	while 1:

		input_list_words = get_input_words()

		write_to_local_graph_json(input_list_words)

		print_to_xdot()

		# output = run_nodes(input_list_words)

		# print("Вывод:", output)

		# # draw_graphviz()

		# f = open('output.json', 'w')
		# f.close()






	# очистка локального графа +

	# бесконечный цикл +

	# 	преобразование входных слов в  список понятий +
	# 	запись связей между понятиями в предложении в локальный граф +
	# 	выполнение поочередно каждого слова в предложении с сохранением результата в общий файл
	# 		при наличии ответа создание новых узлов и связей
	# 		при рекурсивной зависимости выполнение других узлов внутри определения




