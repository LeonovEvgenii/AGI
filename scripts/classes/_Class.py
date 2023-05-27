import os
import json

from scripts.classes.Node import Node

class _Class(Node):
    def __init__(self, word):
        
        super().__init__(word)
        
        self.list_objects = []

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

    

