import os
import json
import sys

# файл используется еще из subrocess, а там другой sys.path
# абсолютные импрорты для добавления в sys.path использовать не хочется
# sys.path.append("/home/evgeniy/git/AGI/scripts/classes")
try:
    from scripts.classes.Node import Node
except ModuleNotFoundError:
    from Node import Node

from scripts.classes._Object import _Object


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

    def add_obj(self, number_in_sentence):

        new_object = _Object(self.name, number_in_sentence)

        self.dict_objects[self.count_obj] = new_object
        new_object.id = self.count_obj
        self.count_obj += 1

    def __str__(self) -> str:
        return "класс: " + self.name
    
    # метод перевода из локального в глобальный, со всеми проверками
    def local_to_global(self):
        pass

    def get_type(self):
        return "_cls"

