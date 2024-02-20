from time import time
from datetime import datetime, timedelta

from scripts.classes.Node import Node

class _Object(Node):

    id = 0

    def __init__(self, class_name, number_in_sentence):
        
        super().__init__(class_name)
        
        # раньше передовался объект класса в конструктор
        # а теперь только имя
        # self.link_class = class_name

        # id нужно выностить в класс
        # если оставить как есть будет только +1 срабатывать один раз
        # даже других _классов
        # если статичноым сделать , на все _объекты
        # распространяться будет.
        # В классе педелать нужно список _объектов на словарь
        # с idшниками

        self.id += 1

        self.number_in_sentence = number_in_sentence

        self.create_unix_time = time()
        readable_time_and_zone = datetime.utcfromtimestamp(self.create_unix_time) + timedelta(hours = 5)
        self.short_readable_time = readable_time_and_zone.strftime('%H:%M:%S')

        # Пока не добавляю в список объектов в файл класса (локальный).
        # Общеснено, почему объеснено в классе _Class

    # def __str__(self):
    #     return self.name + "\t" + self.short_readable_time + "\t" + str(self.number_in_sentence)

    def __str__(self) -> str:
        return "объект: " + self.name

    def get_type(self):
        return "_obj"