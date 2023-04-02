import os
import json

class _Class():
    def __init__(self, word):
        self.name = word
        self.list_objects = []

        # создание файла класса в локальном графе (в любом случае)
        # при смене БД, записи изменяются здесь
        path_to_main = os.path.abspath(os.curdir)
        path_to_local_clasess = path_to_main + "/database_json/local/"
        path_to_file_class = path_to_local_clasess + self.name + ".json"

        json_dic = {}
        json_dic['name'] = self.name
        json_dic['definitions'] = []
        json_dic['objects'] = []
        with open(path_to_file_class, 'w') as outfile:
            json.dump(json_dic, outfile, ensure_ascii=False)
        outfile.close()


    def __str__(self):
        return self.name
    
    # метод перевода из локального в глобальный, со всеми проверками
    def local_to_global(self):
        pass