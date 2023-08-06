import os
import json
import sys

sys.path.append("/home/evgeniy/git/AGI/scripts/classes")
from Node import Node


class _Class(Node):
    def __init__(self, word):
        
        super().__init__(word)
        
        self.dict_objects = {}

        # питоновская программа хранится как имя файла или путь к файлу, т к код в классе
        # не должен меняться. Если делать функциями или импортами, то придется на все определения делать все
        # функции/импорты и они постоянно будут пополняться.
        self.name_python_programm = ""
        self.definitions = []
        self.count_obj = 0

    def add_obj(self, obj):
        self.dict_objects[self.count_obj] = obj
        obj.id = self.count_obj
        self.count_obj += 1

    def __str__(self):
        return self.name
    
    # метод перевода из локального в глобальный, со всеми проверками
    def local_to_global(self):
        pass

    

