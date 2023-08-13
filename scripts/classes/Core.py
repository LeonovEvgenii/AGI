import subprocess
import os
import json

from scripts.classes.Knowledge_base import Knowledge_base
from scripts.classes._Class import _Class
from scripts.classes._Object import _Object
from scripts.classes.Drawer import Drawer

class Core():
    def __init__(self):
        self.kb = Knowledge_base()
        self.drawer = Drawer(self.kb)

        self.clear_local_graph()

    
    def formatting(self, input_str):
        input_str = input_str.lower()

        punctuation = '!"#$%&\'()*,;@[\\]^`{|}~'
        for p in punctuation:
            if p in input_str:
                input_str = input_str.replace(p, '')

        input_list_words = input_str.split(" ")
        
        input_list_words = [ i for i in input_list_words if i ]

        return input_list_words


    def input_words(self):

        while 1:
            input_str = input("Ввод: ")
            if input_str == "":
                print("Введена пустая строка")
                continue

            input_list_words = self.formatting(input_str)

            if input_list_words:
                
                input_objects, input_classes = self.words_to_lists(input_list_words)
                return input_objects, input_classes
                
            else:
                print("Строка не содержит ни одного ключевого слова")


    def words_to_lists(self, input_list_words):

        input_objects = []
        input_classes = []

        for i, word in enumerate(input_list_words):
                    
            class_in_list = False

            for _class in self.kb.local_classes:
                if _class.name == word:
                    new_object = _Object(_class, i + 1)
                    _class.add_obj(new_object)
                    self.kb.create_object(new_object)

                    input_objects.append(new_object)
                    self.kb.local_objects.append(new_object)


                    class_in_list = True
                
            # Проверки на уже существование класса осуществляются только для локального графа.
            # Во время выполненения нод может быть косяк, когда сначала поиск идет по локальному графу
            # потом по глобальному. В слове из локального графа может не оказаться определения.
            # Но логично, что сначала смотрим на локальный граф, т к это последний контекст.
            # Сейчас переход в глобальный осуществляется только по команде в ручном режиме.

            if not class_in_list:
                new_class = _Class(word)

                # если в классах класс и объект создаются и добаляются отдельно,
                # (где то им все равно приходится по отдельности создаваться)
                # то и в базе знаний сделаю отдельные методы для работы с ними
                # так же в данном методе уже производится проверка о необходимости создания класса
                self.kb.create_class(new_class)

                input_classes.append(new_class)
                self.kb.local_classes.append(new_class)

                new_object = _Object(new_class, i + 1)
                new_class.add_obj(new_object) # можно спрятать внутрь конструктора объекта
                self.kb.create_object(new_object)

                # ответить на вопросы:
                # пареметры в функции kb передаются в виде объетов или в виде строк
                # функции kb помимо всего делаемого, возвращают созданный объект
                # содаваться могут class obj py def link, они все возвращаемыми объектами будут
                # проверить не полностью на диалоге секунда
                # может там и другие ключевые слова чинить придется
                # self.kb.create_def("333", [new_object.name, new_object.name])

                input_objects.append(new_object)
                self.kb.local_objects.append(new_object)


        # не забываем, что input_list_classes только новые классы возвращаются
        # если ничего не вернулось, значит они уже есть в local_list_classes
        return input_objects, input_classes


    def test_intput_lists(self, input_objects, input_classes):
        print("список входных объектов")
        [ print(i) for i in input_objects ]
        print("список входных классов")
        [ print(i) for i in input_classes ]

        print("\nсписок локальных объектов")
        [ print(i) for i in self.kb.local_objects ]
        print("список локальных классов")
        [ print(i) for i in self.kb.local_classes ]

    
    def write_local_links(self, input_objects, input_classes):
        
        count_obj = len(input_objects)
        for index, obj in enumerate(input_objects):
            
            if index + 1 != count_obj:
                self.kb.create_local_link(obj, input_objects[index + 1])

        # когда бегу по всем классам, могут быть дубли ссылок из списка введеных классов
        # в прошлой итерации ввода
        # поэтому перехожу на множество ссылок

        # не использую локальные классы, т к в таком случае некоторые связи с классами не обазуются
        for _class in self.kb.local_classes:
            for k, obj in _class.dict_objects.items():
                self.kb.create_local_link(_class, obj)


    def test_links(self):

        # отрисовка пар
        for i in self.kb.local_links:
            print("пара")
            for j in i:
                if j.__class__.__name__ == "_Object":
                    print(j.name, j.id, j.__class__.__name__)
                else:
                    print(j.name, j.__class__.__name__)



    def clear_local_graph(self):
        # print("\nочищаю локальный граф\n")
        self.kb.clear_local_files()
        self.kb.clear_local_links()
        self.drawer.clear_local_dot()

        # f = open('output.json', 'w')
        # f.close()

            

    def run_nodes(self, input_objects, local_classes):

        # ссылка на программу хранится в одноименном файле
        # можно кстати один файл со всем иссылками деражть, но я не знаю какие баги появятся

        # оформить в виде отдельной функции
        # уже написана в кб
        list_name_class_global = [file[:-5] for file in os.listdir(self.kb.path_json_global)]

        list_name_input_object = [obj.name for obj in input_objects]

        for in_obj in input_objects:

            # починить слово "сохрани_определени" как для первородных, так и второродных
            # глобальные определения хранятся в json, тк базу данных я так и не нашел
            # локальные - в полях класса как ссылка на питон, так и определение
            # при переносе в глобальный - записывается из полей в файл

            python_file = ""

            if in_obj.link_class.name_python_programm:
                print("есть в локальном")
                print(in_obj.link_class.name_python_programm)
                # сохраняем путь к программе
            elif in_obj.name in list_name_class_global:
                print("есть в глобальном")

                # это должно быть в классе knoewledge как метод возвращающий путь
                with open(self.kb.path_json_global + in_obj.name + ".json") as json_file:
                    data = json.load(json_file)
                    if "python_file" in data:
                        # сохраняем путь к программе
                        python_file = data["python_file"]

            if python_file:
                # запускаем субпроцесс, выполняем программу, передаем остальные параметры 
                # (передавать ли выполняемое слово как параметр ? )

                path_python = self.kb.path_python_programm + python_file


                # надо что то делать с субпроцессом
                # он накладывает ограничения на принты внутри себя
                # т к только первый принт считается результатом субпроцесса
                # необходимо написать свой модуль выполнения первородных нод
                # в модуль должны приходить путь к файлу, параметры
                # а выходить новые ноды как результат вычислений и ошбки отдельно
                # с этимирезультатами должна работать отрисовка
                # ее походу пора уже в виде сайта делать

                # subprocess блокирует выполнение основной программы, пока дочерний процесс не завершится
                # принятое решение № 19
                output = subprocess.check_output(["python3", path_python] + list_name_input_object, encoding ='utf-8')

                # если слово при выполнении генерирует новые ноды или связи
                # оно возвращает результат в виде текста
                # таким образом каждое слово можно запускать независимо, 
                # передавая ему параметры при необходимости

                # если запускать слово treadingом или multiprcessingом,
                # то не известно когда они закончатся
                # и код в них не может быть изменен

                if output:

                    print("в core", output)

                    output = output.replace('\n', '')
                    list_words = self.formatting(output)
                    generate_objects, generate_classes = self.words_to_lists(list_words)
                    self.write_local_links(generate_objects, generate_classes)


                # Результат возвращается в виде объектов. 
                # Если не объект, то можно подумать убрать субпроцесс. 
                # Еще можно строковый вывод через конструктор объекта пропускать. 
                # Может ли быть несколько возвращенных объектов?
        
                # дополняем локальный граф новыми возвращенными элементами и связями
                
                # вызываем программу "на_что_похоже", пареметры введенное предложение 
                # (можно в локальном, потом в глобальном поиск делать)
                # Выдаем ответ после результата на что похоже, если он не пустой

        


        # path_json_local = os.getcwd() + "/json/local/"
        # path_json_global = os.getcwd() + "/knowledge_base/json_description_words/global/"


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

    
    def compare(self, search_word="два"):
        
        for link in self.kb.local_links:
            pass
        
        return True
