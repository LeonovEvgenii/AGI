import os
import json
import re

import signal
import sys

# это не все существующие функции и приходится импортировать только избранные
from scripts.util.functions import write_to_local_graph_json, save_new_nodes

from scripts.classes.Core import Core


def open_graph(path, core):
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


def run_dialog(path, core):
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
		input_list_words = core.formatting(pair[0])

		print("Ввод: "+pair[0])

		output = core.run_nodes(input_list_words)

		if "рекурсия" not in input_list_words:
			write_to_local_graph_json(input_list_words)
			core.print_to_xdot_local()
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
		

def all_tests(core):

	test_files = os.listdir("dialogs/")

	for file in test_files:
		run_dialog("dialogs/" + file)
		core.clear_local_graph()

# выяснить что это за два параметра
# https://stackoverflow.com/questions/4205317/capture-keyboardinterrupt-in-python-without-try-except
def signal_handler(signal, frame):
    print(' You pressed Ctrl+C! bye bye')
    sys.exit(0)


if __name__ == "__main__":

	signal.signal(signal.SIGINT, signal_handler)

	core = Core()

	# open_graph("graphs/kolobok.dot")

	# временная мера по передаче core параметром
	# решить: сделать функцию частью core и вызывать как метод или оставить в main
	# run_dialog("dialogs/recursion.txt", core)
	# run_dialog("dialogs/second.txt", core)
	# run_dialog("dialogs/year.txt", core)
	# run_dialog("dialogs/history.txt", core) # пока нельзя выполнять, т к нет сравнения текущего вреени с правильным ответом
	# exit(0)

	# core.all_tests(core)
	# exit(0)

	while 1:

		input_objects, input_classes = core.input_words()
		# core.test_intput_lists(input_objects, input_classes)

		# в принятые решения
		# локальный граф не храню в json, т к он все равно чистится при перезапусках.
		# с дебагом без файлов, я надеюсь справлюсь
		# связи образуются между соседними членами предложения, 
		# т к предложение несет логику связи именно этих слов в таком порядке
		# дополнительные связи и порядок образуются при выполнении нод
		core.write_local_links(input_objects, input_classes)
		# core.test_links()

		# сначало выполнение кода, 
		# сгенерированные ответы не всегда записываются в БД
		# в список локальных нод попадают
		# потом запись в БД вместе со сгенерированными ответами

		output = core.run_nodes(input_objects, input_classes)
		

		# попмимо выполнения слов, выполнять операцию сравнения с частью графа. Если есть совпадение
		#  с частью, это возможный ответ.

		# stop_words = ["рекурсия", "удали_из_локального"]

		# flag_print = True
		# for word in input_list_words:
		# 	if word in stop_words:
		# 		flag_print = False

		# if flag_print:
			# write_to_local_graph_json(input_list_words)
			# print_to_xdot_local()
			# save_new_nodes(input_list_words)

		# print("Вывод:", output)

		# f = open('output.json', 'w')
		# f.close()

		core.drawer.print_to_xdot_local()