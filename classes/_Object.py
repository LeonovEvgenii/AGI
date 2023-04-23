from time import time
from datetime import datetime, timedelta

from classes._Class import _Class


class _Object():
    def __init__(self, new_class, number_in_sentence):
        self.link_class = new_class
        self.class_name = new_class.name

        self.number_in_sentence = number_in_sentence

        self.create_unix_time = time()
        readable_time_and_zone = datetime.utcfromtimestamp(self.create_unix_time) + timedelta(hours = 5)
        self.short_readable_time = readable_time_and_zone.strftime('%H:%M:%S')

        # Пока не добавляю в список объектов в файл класса (локальный).
        # Общеснено, почему объеснено в классе _Class

    def __str__(self):
        return self.class_name + "\t" + self.short_readable_time + "\t" + str(self.number_in_sentence)

