# from class_node import Node
import os
import subprocess
import json
import re

# это не все существующие функции и приходится импортировать только избранные
from scripts.util.functions import write_to_local_graph_json, print_to_xdot_local, clear_local_graph, save_new_nodes, get_input_objects_and_classes, proseccing_input_words

path_json_local = os.getcwd() + "/json/local/"
path_json_global = os.getcwd() + "/knowledge_base/json_description_words/global/"

def run_nodes(input_list_objects, local_list_classes):



	# в классе "класс" должна храниться ссылка на python программу
	# проверить на тестовй программе, типа print("1"), что она работает
	# запихать в "палка" временно
	# проходим по списку и выходим, т к в палке кода не должно быть


	# + Взять список локальных слов
	# Взять список глобальных слов (позже)
	# очистка от расширения .json
	list_name_class_global = [file[:-5] for file in os.listdir(path_json_global)]

	list_name_input_object = [obj.class_name for obj in input_list_objects]

	# Цикл по всем входным словам
	for in_obj in input_list_objects:
		# print(in_obj.class_name)
		# необходимо создать тестовый файл с определением в глобальном графе и локальном
		# Может для переноса в глобальный функцию в классе запилить
		# Можно служебное слово "сохрани_определение" для локального
		# с глобального проще начать, файл я создам для примера руками
		# использование служебного слова еще не готова, но тоже надо проверять
		# как будут храниться сохраненные локальные опрееления, пусть даже первородные ?
		# - в поле класса в списке храниться

		python_file = ""

		# У введенного слова есть код 
		# (введенные слова всегда в локальном списке есть, они же только что ввелись)
		if in_obj.link_class.name_python_programm:
			print("есть в локальном")
			print(in_obj.link_class.name_python_programm)
			# сохраняем путь к программе

		# иначе, есть в глобальном списке
		elif in_obj.class_name in list_name_class_global:
			print("есть в глобальном")

			# это должно быть в классе knoewledge как метод возвращающий путь
			with open(os.getcwd() + "/knowledge_base/json_description_words/global/" + in_obj.class_name + ".json") as json_file:
				data = json.load(json_file)
				if "python_file" in data:
					# сохраняем путь к программе
					python_file = data["python_file"]

		if python_file:
			# запускаем субпроцесс, выполняем программу, передаем остальные параметры (передавать ли выполняемое слово как параметр ? )

			path_python = os.getcwd() + "/knowledge_base/python_programm/" + python_file

			output = subprocess.check_output(["python3", path_python] + list_name_input_object, encoding='utf-8')

			print(output)

			# Результат возвращается в виде объектов. 
			# Если не объект, то можно подумать убрать субпроцесс. 
			# Еще можно строковый вывод через конструктор объекта пропускать. 
			# Может ли быть несколько возвращенных объектов?
	
			# дополняем локальный граф новыми возвращенными элементами и связями
			
			# вызываем программу "на_что_похоже", пареметры введенное предложение (можно в локальном, потом в глобальном поиск делать)
			# Выдаем ответ после результата на что похоже, если он не пустой
			# Позже завести класс Core и занести все основные фунции манипуляции с нодами туда. В main оставить запуски, тесты.



	# обработка последовательная т к при параллельной дублирование

	# output = ""

	# list_local_json_files = os.listdir(path_json_local)
	# list_globa_json_files = os.listdir(path_json_global)
	# list_all_json_files = list(set(list_local_json_files + list_globa_json_files))

	# path_python = os.getcwd() + "/python_programm"

	# global_output = ""

	# for i, word in enumerate(input_list_words):

	# 	for file in list_all_json_files:

	# 		word_class = word[:word.rfind("$")]

	# 		if word_class == file[:-5]:

	# 			if file in list_globa_json_files:
	# 				json_file = open(path_json_global + file)
	# 			elif file in list_local_json_files:
	# 				json_file = open(path_json_local + file)
	# 			else:
	# 				continue
					
	# 			data = json.load(json_file)

	# 			# если нет питона то не выполняем, а так все слова в предложении выполняются
	# 			if "file" in data:
	# 				list_without_run_word = input_list_words.copy()
	# 				list_without_run_word.remove(word)

	# 				output = subprocess.check_output(["python3", path_python + "/" + data["file"]] + list_without_run_word, encoding='utf-8')

	# 				# проверка, если удалялись файлы, актуализировать из список
	# 				if os.stat(os.getcwd() + "/output.json").st_size != 0:
	# 					# не пустой файл
	# 					with open(os.getcwd() + "/output.json") as json_file:
	# 						data = json.load(json_file)

	# 						if "файл_удален" in data:
	# 							if data["файл_удален"] == True:
	# 								list_local_json_files = os.listdir(path_json_local)
	# 								list_globa_json_files = os.listdir(path_json_global)
	# 								list_all_json_files = list(set(list_local_json_files + list_globa_json_files))
	# 								continue
	# 						json_file.close()

	# 				if output:
	# 					output = output.replace("\n", "")
	# 					output_list_words = [word_class] # !!!  экземпляр скорей всеого придется по новому делать. Раньше класс делался.
	# 					output_list_words += output.split(" ")
	# 					save_new_nodes(output_list_words)
	# 					if word_class != "рекурсия":
	# 						write_to_local_graph_json(output_list_words)
	# 						print_to_xdot_local()
	# 					global_output += " "
	# 					global_output += output
	# 			json_file.close()

	# global_output = global_output.strip()

	# return global_output


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
	# run_dialog("dialogs/history.txt") # пока нельзя выполнять, т к нет сравнения текущего вреени с правильным ответом
	# exit(0)

	# all_tests()
	# exit(0)

	local_list_objects = []
	local_list_classes = []

	while 1:

		input_list_objects, input_list_classes = get_input_objects_and_classes(local_list_objects, local_list_classes)

		# не забываем, что input_list_classes только новые классы возвращаются
		# если ничего не вернулось, значит они уже есть в local_list_classes

		# print("список входных объектов")
		# [ print(i) for i in input_list_objects ]
		# print("список входных классов")
		# [ print(i) for i in input_list_classes ]

		# print("\nсписок локальных объектов")
		# [ print(i) for i in local_list_objects ]
		# print("список локальных классов")
		# [ print(i) for i in local_list_classes ]

		# сначало выполнение кода, 
		# сгенерированные ответы не всегда записываются в БД
		# в список локальных нод попадают
		# потом запись в БД вместе со сгенерированными ответами

		# хранение графа в локальном фале в этом участке кода не делаю
		# его можно сделать после или при выполненни нод,
		# т к последовательность в предложении есть и пары можно и там образовать
		
		# Помнится, ты примнал решение всегда образовывать пары после ввода

		# write_link_to_local_graph_json(input_list_words)

		# может локальный граф целиком в массивах хранить, все равно при каждом перезапуске чистится

		output = run_nodes(input_list_objects, local_list_classes)
		

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

		# xdot так то проще полностью перезаписвывать и не мелочиться
		print_to_xdot_local(local_list_classes)