from time import time
from datetime import datetime, timedelta

from scripts.classes._Class import _Class
from scripts.classes.Node import Node

class _Object(Node):
    def __init__(self, new_class, number_in_sentence):
        
        super().__init__(new_class.name)
        
        self.link_class = new_class

        self.id = None

        self.number_in_sentence = number_in_sentence

        self.create_unix_time = time()
        readable_time_and_zone = datetime.utcfromtimestamp(self.create_unix_time) + timedelta(hours = 5)
        self.short_readable_time = readable_time_and_zone.strftime('%H:%M:%S')

        # Пока не добавляю в список объектов в файл класса (локальный).
        # Общеснено, почему объеснено в классе _Class

    # def __str__(self):
    #     return self.name + "\t" + self.short_readable_time + "\t" + str(self.number_in_sentence)

