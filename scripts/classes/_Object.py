from time import time
from datetime import datetime, timedelta

from scripts.classes.Node import Node

class _Object(Node):
    def __init__(self, class_name, number_in_sentence):
        
        super().__init__(class_name)
        
        # раньше передовался объект класса в конструктор
        # а теперь только имя
        # self.link_class = class_name

        self.id = None

        self.number_in_sentence = number_in_sentence

        self.create_unix_time = time()
        readable_time_and_zone = datetime.utcfromtimestamp(self.create_unix_time) + timedelta(hours = 5)
        self.short_readable_time = readable_time_and_zone.strftime('%H:%M:%S')

        # Пока не добавляю в список объектов в файл класса (локальный).
        # Общеснено, почему объеснено в классе _Class

    # def __str__(self):
    #     return self.name + "\t" + self.short_readable_time + "\t" + str(self.number_in_sentence)

    def get_type(self):
        return "_obj"