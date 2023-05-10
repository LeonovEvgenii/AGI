import os
import json

from scripts.classes.Node import Node

class _Class(Node):
    def __init__(self, word):
        self.name = word
        self.list_objects = []

        # self.create_empty_local_file_class()

        # питоновская программа хранится как имя файла или путь к файлу, т к код в классе
        # не должен меняться. Если делать функциями или импортами, то придется на все определения делать все
        # функции/импорты и они постоянно будут пополняться.
        self.name_python_programm = ""
        self.definitions = []


    def __str__(self):
        return self.name
    
    # метод перевода из локального в глобальный, со всеми проверками
    def local_to_global(self):
        pass

    def create_empty_local_file_class(self):

        # создание файла класса в локальном графе (в любом случае)
        # при смене БД, записи изменяются здесь
        # по идее, в локальный граф можно вообще не писать ничего в фалы или БД,
        # т к при перезапуске он все равно чистится.
        # Нужен только метод перевода в глобальный.
        
        path_to_main = os.path.abspath(os.curdir)
        path_to_local_clasess = path_to_main + "/database_json/local/"
        path_to_file_class = path_to_local_clasess + self.name + ".json"

        json_dic = {}
        json_dic['name'] = self.name
        json_dic['definitions'] = []
        json_dic['objects'] = []
        with open(path_to_file_class, 'w') as outfile:
            json.dump(json_dic, outfile, ensure_ascii=False)
        outfile.close()

