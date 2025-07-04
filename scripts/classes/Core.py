"""Файл класса Core."""

import json
import os
import subprocess

from scripts.classes.Knowledge_base import Knowledge_base  # !!! убрать
from scripts.classes.conversion.Console import Console


class Core():
    """Класс с основными операциями над понятиями."""

    def __init__(self):
        """."""
        self.console = Console()

        self.kb = Knowledge_base()

        # Выполнить поиск по методу и убрать в kb.
        # self.clear_local_graph()

    def run_nodes(self, input_objects, local_classes):
        """Основной метод выполнения кода в понятиях."""
        # ссылка на программу хранится в одноименном файле
        # можно кстати один файл со всеми ссылками держать, но я не знаю какие
        # баги появятся

        # оформить в виде отдельной функции
        # уже написана в кб
        list_name_class_global = [
            file[:-5] for file in os.listdir(self.kb.path_json_global)
        ]

        list_name_input_object = [obj.name for obj in input_objects]

        for in_obj in input_objects:

            # починить слово "сохрани_определение" как для первородных, так и
            # второродных
            # глобальные определения хранятся в json, тк базу данных я так и
            # не нашел
            # локальные - в полях класса как ссылка на питон, так и определение
            # при переносе в глобальный - записывается из полей в файл

            python_file = ''

            if in_obj.link_class.name_python_program:
                # print("есть в локальном")
                print(in_obj.link_class.name_python_program)
                # сохраняем путь к программе
            elif in_obj.name in list_name_class_global:
                # print("есть в глобальном")

                # это должно быть в классе knowledge как метод возвращающий
                # путь
                with open(
                        self.kb.path_json_global + in_obj.name + '.json'
                ) as json_file:
                    data = json.load(json_file)
                    if 'python_file' in data:
                        # сохраняем путь к программе
                        python_file = data['python_file']

            if python_file:
                # запускаем субпроцесс, выполняем программу, передаем
                # остальные параметры
                # (передавать ли выполняемое слово как параметр ? )

                path_python = self.kb.path_python_program + python_file

                # надо что то делать с субпроцессом
                # он накладывает ограничения на принты внутри себя
                # т к только первый принт считается результатом субпроцесса
                # необходимо написать свой модуль выполнения первородных нод
                # в модуль должны приходить путь к файлу, параметры
                # а выходить новые ноды как результат вычислений и ошибки
                # отдельно
                # с этими результатами должна работать отрисовка
                # ее походу пора уже в виде сайта делать

                # subprocess блокирует выполнение основной программы, пока
                # дочерний процесс не завершится
                # принятое решение № 19
                output = subprocess.check_output(
                    ['python3', path_python] + list_name_input_object,
                    encoding='utf-8')

                # если слово при выполнении генерирует новые ноды или связи
                # оно возвращает результат в виде текста
                # таким образом каждое слово можно запускать независимо,
                # передавая ему параметры при необходимости

                # если запускать слово treadingом или multiprcessingом,
                # то не известно когда они закончатся
                # и код в них не может быть изменен

                if output:

                    print('в core', output)

                    output = output.replace('\n', '')
                    list_words = self.formatting(output)
                    generate_objects, generate_classes = self.words_to_lists(
                        list_words)
                    # устаревший метод, удалил (write_local_links)
                    self.write_local_links(generate_objects, generate_classes)

                # Результат возвращается в виде объектов.
                # Если не объект, то можно подумать убрать субпроцесс.
                # Еще можно строковый вывод через конструктор объекта
                # пропускать.
                # Может ли быть несколько возвращенных объектов?

                # дополняем локальный граф новыми возвращенными элементами и
                # связями

                # вызываем программу "на_что_похоже", параметры введенное
                # предложение
                # (можно в локальном, потом в глобальном поиск делать)
                # Выдаем ответ после результата на что похоже, если он не
                # пустой

        # path_json_local = os.getcwd() + "/json/local/"

        # path_json_global = os.path.join(
        #     os.getcwd(),
        #     'knowledge_base',
        #     'json_description_words',
        #     'global'
        # )

        # обработка последовательная т к при параллельной дублирование

        # output = ""

        # list_local_json_files = os.listdir(path_json_local)
        # list_global_json_files = os.listdir(path_json_global)
        # list_all_json_files = list(
        #     set(list_local_json_files + list_global_json_files)
        # )

        # path_python = os.getcwd() + "/python_program"

        # global_output = ""

        # for i, word in enumerate(input_list_words):

        # 	for file in list_all_json_files:

        # 		word_class = word[:word.rfind("$")]

        # 		if word_class == file[:-5]:

        # 			if file in list_global_json_files:
        # 				json_file = open(path_json_global + file)
        # 			elif file in list_local_json_files:
        # 				json_file = open(path_json_local + file)
        # 			else:
        # 				continue

        # 			data = json.load(json_file)

        # 			# если нет питона то не выполняем, а так все слова в предложении
        #           # выполняются
        # 			if "file" in data:
        # 				list_without_run_word = input_list_words.copy()
        # 				list_without_run_word.remove(word)

        #               output = subprocess.check_output(
        #                   ["python3", path_python + "/" + data["file"]] +
        #                   list_without_run_word,
        #                   encoding='utf-8'
        #               )

        # 				# проверка, если удалялись файлы, актуализировать из список
        # 				if os.stat(os.getcwd() + "/output.json").st_size != 0:
        # 					# не пустой файл
        # 					with open(os.getcwd() + "/output.json") as json_file:
        # 						data = json.load(json_file)

        # 						if "файл_удален" in data:
        # 							if data["файл_удален"] == True:
        # 								list_local_json_files = os.listdir(path_json_local)
        # 								list_global_json_files = os.listdir(path_json_global)
        #                               list_all_json_files = list(set(
        #                                   list_local_json_files + list_global_json_files
        #                               ))
        # 								continue
        # 						json_file.close()

        # 				if output:
        # 					output = output.replace("\n", "")
        # 					# !!!  экземпляр скорей всего придется по новому делать.
        #                   # Раньше класс делался.
        #                   output_list_words = [word_class]
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

    def run_nodes_2(self, input_graph):
        """Вторая итерация рефакторинга метода."""
        # работа с локальным графом, глобальным и контекстом
        # контекст может быть на уровне консоли, может быть на уровне run_node

        return input_graph

    def run_node(self, node):
        """Выполнение одной ноды."""
        # Алгоритм.
        # Если нода второродная, рекурсивно проваливаемся.
        # Если первородная, выполняем определение.

        output_graphs = self.__exec_python(node.path_python_file)

        return output_graphs

    def __exec_python(self, path):
        # пока не передаю параметры командной строки для вычислений внутри
        output = subprocess.check_output(
            ['python3', path],
            encoding='utf-8')

        output_graphs = self.console.content_to_graphs(output)

        return output_graphs

    def compare(self, input_objects, input_classes, search_word='два'):
        """Метод сравнения кусков графа."""
        all_input = input_objects + input_classes

        all_types = ['_object', '_class']

        words_def = self.kb.read_defs(search_word)[0]

        res = []

        for def_word in words_def:
            for input_word in all_input:

                if def_word in all_types:
                    # print(
                    #     input_word.name,
                    #     type(input_word),
                    #     'сравниваю по типу с ',
                    #     def_word
                    #     )

                    end_type = str(type(input_word)).split('.')[-1]
                    end_type = end_type[:-2].lower()

                    if end_type == def_word:
                        res.append(True)
                        print(input_word.name)
                        print(type(input_word))
                        print(True)
                        print()
                        break
                    else:
                        res.append(False)
                        print(input_word.name)
                        print(type(input_word))
                        print(False)
                        print()
                        all_input.remove(input_word)

                else:
                    print(
                        input_word.name,
                        'сравниваю по названию с ',
                        def_word
                    )
                    # сравнение названий
                    pass

        print(res)
