import os
import json

from scripts.classes.Node import Node

class _Class(Node):
    def __init__(self, word, path_json_local):
        
        super().__init__(word)
        
        self.list_objects = []

        # питоновская программа хранится как имя файла или путь к файлу, т к код в классе
        # не должен меняться. Если делать функциями или импортами, то придется на все определения делать все
        # функции/импорты и они постоянно будут пополняться.
        self.name_python_programm = ""
        self.definitions = []

        self.path_json_local = path_json_local

        self.create_file()

    def __str__(self):
        return self.name
    
    # метод перевода из локального в глобальный, со всеми проверками
    def local_to_global(self):
        pass

    def create_file(self):

        # При смене БД, записи изменяются здесь.
        # файлы пишутся, т к вызываются через субпроцесс и должны иметь доступ к БД
        # БД сейчас это файлы

        
        file_name = self.path_json_local + self.name + ".json"

        json_dic = {}
        json_dic['name'] = self.name
        json_dic['definitions'] = []
        json_dic['objects'] = []
        with open(file_name, 'w') as outfile:
            json.dump(json_dic, outfile, ensure_ascii=False)
        outfile.close()

