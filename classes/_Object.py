from time import time
from datetime import datetime, timedelta

class _Object():
    def __init__(self, word, number_in_sentence):
        self._class = word # ссылка на класс должна быть

        # проверка на существование класса в общем списке в монго
        # здесь же запись в монго объектов
        # решить локально или глобально


        self.number_in_sentence = number_in_sentence

        self.create_unix_time = time()
        readable_time_and_zone = datetime.utcfromtimestamp(self.create_unix_time) + timedelta(hours = 5)
        self.short_readable_time = readable_time_and_zone.strftime('%H:%M:%S')


    def __str__(self):
        return self._class + "\t" + self.short_readable_time + "\t" + str(self.number_in_sentence)

