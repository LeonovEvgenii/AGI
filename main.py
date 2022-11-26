# from class_node import Node
import os
import subprocess
import json
import re

from util.functions import write_to_local_graph_json, print_to_xdot_local, clear_local_graph

path_json_local = os.getcwd() + "/json/local/"
path_json_global = os.getcwd() + "/json/global/"

def proseccing_input_words(input_str):
	input_str = input_str.lower()

	punctuation = '!"#$%&\'()*,-/;<=>@[\\]^`{|}~'
	for p in punctuation:
		if p in input_str:
			input_str = input_str.replace(p, '')

	input_list_words = input_str.split(" ")
	
	input_list_words = [ i for i in input_list_words if i]

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


def run_nodes(input_list_words):

	# обработка последовательная т к при параллельной дублирование

	output = ""

	list_local_json_files = os.listdir(path_json_local)
	list_globa_json_files = os.listdir(path_json_global)
	list_all_json_files = list(set(list_local_json_files + list_globa_json_files))

	path_python = os.getcwd() + "/python_programm"

	global_output = ""

	for i, word in enumerate(input_list_words):

		for file in list_all_json_files:
			if word == file[:-5]:

				if file in list_globa_json_files:
					json_file = open(path_json_global + file)
				elif file in list_local_json_files:
					json_file = open(path_json_local + file)
				else:
					continue
					
				data = json.load(json_file)

				# если нет питона то не выполняем, а так все слова в предложении выполняются
				if "file" in data:
					list_without_run_word = input_list_words.copy()
					list_without_run_word.remove(word)

					output = subprocess.check_output(["python3", path_python + "/" + data["file"]] + list_without_run_word, encoding='utf-8')

					# проверка, если удалялись файлы, актуализировать из список
					if os.stat(os.getcwd() + "/output.json").st_size != 0:
						# не пустой файл
						with open(os.getcwd() + "/output.json") as json_file:
							data = json.load(json_file)

							if "файл_удален" in data:
								if data["файл_удален"] == True:
									list_local_json_files = os.listdir(path_json_local)
									list_globa_json_files = os.listdir(path_json_global)
									list_all_json_files = list(set(list_local_json_files + list_globa_json_files))
									continue
							json_file.close()

					if output:
						output = output.replace("\n", "")
						output_list_words = [word]
						output_list_words += output.split(" ")
						save_new_nodes(output_list_words)
						if word != "рекурсия":
							write_to_local_graph_json(output_list_words)
							print_to_xdot_local()
						global_output += " "
						global_output += output
				json_file.close()

	global_output = global_output.strip()

	return global_output


def save_new_nodes(input_list_words):

	files = os.listdir(path_json_local)
	for word in input_list_words:
		if not word + ".json" in files:
			defenition = {}
			defenition['name'] = word
			with open("json/local/" + word + ".json", 'w') as outfile:
				json.dump(defenition, outfile, ensure_ascii=False)
			outfile.close()


def open_graph(path):
	lines = None
	with open(path, "r") as original_file:
		lines = original_file.readlines()
	original_file.close()

	data_json = []
	for line in lines:
		match = re.findall(r'"(.*)".{0,}(->|--).{0,}"(.*)";{0,}', line)
		if match != []:
			tmp = [match[0][0], match[0][2]]
			data_json.append(tmp)

	with open("graphs/local_graph.json", 'w') as json_file:
		json.dump(data_json, json_file, ensure_ascii=False)
	json_file.close()

	with open('graphs/local_graph.dot', 'w') as write_file_graph:
		for line in lines:
			write_file_graph.write(line)
	write_file_graph.close()


def run_dialog(path):
	lines = None
	with open(path, "r") as dialog_file:
		lines = dialog_file.readlines()
	dialog_file.close()

	pair = []
	pairs = []

	for line in lines:
		if "Ввод: " in line:
			strip = line[6:-1]
			pair.append(strip)
		if "Вывод: " in line:
			strip = line[7:-1]
			pair.append(strip)
			pairs.append(pair)
			pair = []

	for pair in pairs:
		input_list_words = proseccing_input_words(pair[0])

		print("Ввод: "+pair[0])

		output = run_nodes(input_list_words)

		if "рекурсия" not in input_list_words:
			write_to_local_graph_json(input_list_words)
			print_to_xdot_local()
			save_new_nodes(input_list_words)


		if pair[1] != output:
			print("\nожидаемый ответ < " + str(pair[1]) + " > не соответсвует полученному < " + str(output) + " >\n")
			print("перываю выполнение")
			return
		else:
			print("Вывод: "+pair[1])

		f = open('output.json', 'w')
		f.close()

	print("\nдиалог выполнился\n")
		

def all_tests():

	test_files = os.listdir("dialogs/")

	for file in test_files:
		run_dialog("dialogs/" + file)
		clear_local_graph()


if __name__ == "__main__":

	clear_local_graph()

	# open_graph("graphs/kolobok.dot")

	# run_dialog("dialogs/recursion.txt")
	# run_dialog("dialogs/second.txt")
	# run_dialog("dialogs/year.txt")
	# exit(0)

	# all_tests()
	# exit(0)

	while 1:

		input_list_words = get_input_words()

		output = run_nodes(input_list_words)

		stop_words = ["рекурсия", "удали_из_локального"]

		flag_print = True
		for word in input_list_words:
			if word in stop_words:
				flag_print = False

		if flag_print:
			write_to_local_graph_json(input_list_words)
			print_to_xdot_local()
			save_new_nodes(input_list_words)

		print("Вывод:", output)

		f = open('output.json', 'w')
		f.close()

