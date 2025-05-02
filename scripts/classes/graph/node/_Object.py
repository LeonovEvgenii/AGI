# Возможно, на файл с нижним подчеркиванием не нужно писать docstring flake8

from datetime import datetime, timezone
from time import time

from scripts.classes.graph.node.Node import Node


class _Object(Node):

    # поле отвечающее за уникальность объектов
    # его значение берется от счетчика новых объектов в классе _Class
    id

    def __init__(self, class_name, number_in_sentence):

        super().__init__(class_name)

        # раньше передавался объект класса в конструктор
        # а теперь только имя
        # self.link_class = class_name

        self.number_in_sentence = number_in_sentence

        self.unix_time = time()
        readable_time_and_zone = datetime.fromtimestamp(
            self.unix_time,
            tz=timezone.utc
        )
        self.short_readable_time = readable_time_and_zone.strftime('%H:%M:%S')

        # Пока не добавляю в список объектов в файл класса (локальный).
        # Почему объяснено в классе _Class

    # def __str__(self):
    #     return (self.name + '\t' + self.short_readable_time + '\t'
    #             + str(self.number_in_sentence))

    def __str__(self) -> str:
        return 'объект: ' + self.name

    def get_type(self):
        return '_obj'
