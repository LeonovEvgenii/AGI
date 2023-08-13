import os
import json
import sys

# файл используется еще из subrocess, а там другой sys.path
# абсолютные импрорты для добавления в sys.path использовать не хочется
# sys.path.append("/home/evgeniy/git/AGI/scripts/classes")
try:
    from scripts.classes._Class import _Class
except ModuleNotFoundError:
    from _Class import _Class


class Knowledge_base():
    def __init__(self):
        
        # дискуссионный вопрос о том, какой тип стурктуры должен быть.
        # точно не словарь, т к дубли по названию не допустимы
        # операции над множествами не планируются
        # поэтому остается список

        # в принятые решения
        # удобно иметь как резделение на классы и объекты
        # так же удобно иметь весь список нод
        # пока оставлю оба варианта, надеюсь багов при переключении все отловлю
        self.local_nodes = []
        self.local_objects = [] 
        self.local_classes = []

        self.local_links = set()

        path_to_workspace = os.getcwd()

        self.path_json_local = path_to_workspace + "/knowledge_base/json_description_words/local/"
        self.path_json_global = path_to_workspace + "/knowledge_base/json_description_words/global/"
        
        self.path_links_local = path_to_workspace + "/knowledge_base/graphs_links/local_graph.json"
        
        self.path_python_programm = path_to_workspace + "/knowledge_base/python_programm/"

    def json_to_data(self, path):
        data = None
        with open(path) as json_file:
            data = json.load(json_file)
            json_file.close()
        return data

    def data_to_json(self, path, data):
        with open(path, 'w') as outfile:
            json.dump(data, outfile, ensure_ascii=False)
            outfile.close()

    # внутри всех методов в kb делать проверку/преобразование из строки в объект
    # пример в методе create_class

    # структура методов
    # группы
    # create
    # update
    # read
    # del
    # exist

    # подгруппы через подчеркивание
    # class
    # obj
    # py
    # def
    # link

    # например
    # create_class
    # read_py

    # по идее все что связано с классом более общное
    # obj py def link  можно перегрузить по типу данных функции, но в питоне с этим проблемы

    # принятое решение № 20, 21
    # принятые решения хотя бы раз сюда продублировать или хотя бы самому прочитать, для освежения в памяти
    # сделать перегузку по типу строка и по готовому объекту
    def create_class(self, new_class):

        if str(type(new_class)) == "<class 'str'>":
            new_class = _Class(new_class)

        file_name = self.path_json_local + new_class.name + ".json"

        json_dic = {}
        json_dic['name'] = new_class.name
        json_dic['definitions'] = []
        json_dic['objects'] = {}
        json_dic['python_file'] = ""

        self.data_to_json(file_name, json_dic)

    def create_object(self, new_obj):
        
        file_name = self.path_json_local + new_obj.name + ".json"

        data = self.json_to_data(file_name)

        json_obj = {}
        json_obj['short_readable_time'] = new_obj.short_readable_time
        # можно так то и другие поля сериализовывать

        data['objects'][new_obj.id] = json_obj

        self.data_to_json(file_name, data)

    def create_local_link(self, obj_1, obj_2):

        # кортеж, чтобы избавиться от ошибки unhashable type:list
        pair = tuple([obj_1, obj_2])
        # не получится ли при этом ситуации, когда понядобятся обновленные поля класса ?

        # возможная проверка на недопущение дублей пар
        # есть пробелема, но это не точно что set setов делать нелзя
        # по хорошему, local_links сделать множеством, т к оно больше,
        # а перед добалением искать возможную дублирующую пару (для (a, b) искать (b, a) и не добалять вторую)
        
        if pair not in self.local_links:
            self.local_links.add(pair)

            data = self.json_to_data(self.path_links_local)

            pair_for_json = []
            element_1 = None
            element_2 = None

            if obj_1.__class__.__name__ == "_Class":
                element_1 = [obj_1.name, "_Class"]
            else:
                element_1 = [obj_1.name, "_Object", obj_1.id]

            if obj_2.__class__.__name__ == "_Class":
                element_2 = [obj_2.name, "_Class"]
            else:
                element_2 = [obj_2.name, "_Object", obj_2.id]

            pair_for_json.append(element_1)
            pair_for_json.append(element_2)

            data['links'].append(pair_for_json)

            self.data_to_json(self.path_links_local, data)

        # проверка на существование элемнта не нужна
        # т к из за разного времени ввода экземпляры класса объект всегда будут разные
        # даже если делать проверку, то через оператор in, а не через set в общем списке связей

        # хрнаить ссылки нужно именно в классах, т к в них все поля содержатся
        # если сделаем свою сериализацию этих полей, то это двойная работа

    # можно передавать в параметры, слова можно объекты
    def create_def(self, class_name, list_words):

        # во все create нужно добавить проверку на существование создаваемого объекта

        if not self.class_exist(class_name):
            self.create_class(class_name)
        elif self.py_exist(class_name):
            # эти ошибки нужно обрабатывать как-то по другому
            # сейчас субпросесс, поэтому все валится в ноды,
            # а должно в отдельный поток ошибок
            # и exit(-1) нельзя дать т к этот код может вполняться не только в субпроцессе
            print("уже существует определение на py")
        
        file_name = self.path_json_local + class_name + ".json"
        dict_class = self.json_to_data(file_name)
        dict_class['definitions'].append(list_words)
        self.data_to_json(file_name, dict_class)

    def create_py(self, class_name, file_py):

        if not self.class_exist(class_name):
            self.create_class(class_name)
        elif self.def_exist(class_name):
            # эти ошибки нужно обрабатывать как-то по другому
            # сейчас субпросесс, поэтому все валится в ноды,
            # а должно в отдельный поток ошибок
            # и exit(-1) нельзя дать т к этот код может вполняться не только в субпроцессе
            print("уже существует обычное определение")


        file_name_class = self.path_json_local + class_name + ".json"
        dict_class = self.json_to_data(file_name_class)
        dict_class["python_file"] = file_py
        self.data_to_json(file_name_class, dict_class)

    def read_class(self, name):
        file_name = self.path_json_local + name + ".json"
        return self.json_to_data(file_name)


    def get_names_local(self):
        return [file[:-5] for file in os.listdir(self.path_json_local)]
    
    def get_names_global(self):
        return [file[:-5] for file in os.listdir(self.path_json_global)]

    def class_exist(self, class_name):

        if class_name in self.get_names_local():
            return True
        elif class_name in self.get_names_global():
            return True
        
        return False

    def def_exist(self, class_name):
        dict_class = self.read_class(class_name)
        if len(dict_class["definitions"]) > 0:
            return True
        else:
            return False

    def py_exist(self, class_name):
        dict_class = self.read_class(class_name)
        if dict_class["python_file"] != "":
            return True
        else:
            return False


    def clear_local_files(self):
        local_files = os.listdir(self.path_json_local)
        if local_files:
            os.system("rm " + self.path_json_local + "*")

    def clear_local_links(self):

        data = {}
        data['links'] = []

        self.data_to_json(self.path_links_local, data)
        
