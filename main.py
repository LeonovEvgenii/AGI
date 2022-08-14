from class_node import Node
import re
import os
import subprocess
import json

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
	
	path_json = os.getcwd() + "/json"
	json_files = os.listdir(path_json)

	path_python = os.getcwd() + "/python_programm"

	for i, word in enumerate(input_list_words):

		for file in json_files:
			if word == file[:-5]:
				with open("json/" + file) as json_file:
					data = json.load(json_file)

					list_without_run_word = input_list_words.copy()
					list_without_run_word.remove(word)

					output = subprocess.check_output(["python3", path_python + "/" + data["file"]] + list_without_run_word, encoding='utf-8')

					print(output)




					# output_string = str(output)

					# output_list = output_string.split(r'\r\n')

					# for e in output_list:
					# 	print(e)

					# print(output.decode('utf-8'))


	# сохранение всех параметров строки
	# открытие и запуск программы с параметрами



if __name__ == "__main__":

	while 1:

		input_list_words = get_input_words()

		run_nodes(input_list_words)

		exit(0)

		

		if "создай новое определение первого рода: " in input_str:
			# definition_mode = True
			input_str = input_str[39:] # 39, пототому что команда константой задана

			input_list_words = input_str.split(" ")

			# сейчас работает только один шаблон "слово file.py"
			defenition = {}
			defenition_name = input_list_words[0]
			defenition['name'] = defenition_name
			defenition['file'] = input_list_words[1]

			with open("json/" + defenition_name + ".json", 'w') as outfile:
				json.dump(defenition, outfile, ensure_ascii=False)

		# подумать над выполнением команды "сохрани время"
		# сохрани тоже превородное, вопрос в том, как папраметры передаются
		

		if "дай определение: " in input_str:
			# question_mode = False
			input_str = input_str[17:]
			
			input_list_words = input_str.split(" ")

			path = os.getcwd() + "/json"
			files = os.listdir(path)
			for file in files:
				if input_list_words[0] == file[:-5]:
					with open("json/" + file) as json_file:
						data = json.load(json_file)
						
						path = os.getcwd() + "/python_programm"
						output = subprocess.check_output(["python3", path + "/" + data["file"]])
						output = str(output)[2:-3]

						print("Вывод: " + output)

		input_list_words = input_str.split(" ")

		input_list_words = [ i for i in input_list_words if i]

		input_list_nodes = convert_words_to_nodes(input_list_words)

		# if question_mode:
			# pass
			# run_programm(input_list_nodes, graph_list_nodes)
			# run_node(input_list_nodes, graph_list_nodes)
			# read_node_to_graph(input_list_nodes, graph_list_nodes)
		# else:
			# graph_list_nodes = add_node_to_graph(input_list_nodes, graph_list_nodes)
			# graph_list_nodes = delete_node_to_graph(input_list_nodes, graph_list_nodes)

			# write_to_graph(graph_list_nodes, file_name)

