import os
import json

class Knowledge_base():
    def __init__(self):
        
        # дискуссионный вопрос о том, какой тип стурктуры должен быть.
        # точно не словарь, т к дубли по названию не допустимы
        # операции над множествами не планируются
        # поэтому остается список

        # в принятые решения
        # удобно иметь как резделение на классы и объекты
        # так же удобно иметь весь список нод
        # пока оставлю оба варианта, надеюсь багов при переключении все отловлю
        self.local_nodes = []
        self.local_objects = [] 
        self.local_classes = []

        self.local_links = []

        self.path_json_local = os.getcwd() + "/knowledge_base/json_description_words/local/"
        self.path_json_global = os.getcwd() + "/knowledge_base/json_description_words/global/"
        self.path_python_programm = os.getcwd() + "/knowledge_base/python_programm/"


    def create_local_link(self, obj_1, obj_2):

        pair = [obj_1, obj_2]

        # возможная проверка на недопущение дублей пар
        # есть пробелема, но это не точно что set setов делать нелзя
        # по хорошему, local_links сделать множеством, т к оно больше,
        # а перед добалением искать возможную дублирующую пару (для (a, b) искать (b, a) и не добалять вторую)
        self.local_links.append(pair)

        # проверка на существование элемнта не нужна
        # т к из за разного времени ввода экземпляры класса объект всегда будут разные
        # даже если делать проверку, то через оператор in, а не через set в общем списке связей


    # структура методов
    # группы
    # add
    # update
    # read
    # del

    # подгруппы через подчеркивание
    # class
    # obj
    # py
    # def
    # link

    # например
    # add_class
    # read_py

    # по идее все что связано с классом более общное
    # obj py def link  можно перегрузить по типу данных функции, но в питоне с этим проблемы
    

    # принятое решение № 20, 21
    def create_class(self, new_class):

        # работаю не со всеми типами нод, а только с классами
        # могут быть ноды второродне, первородне
        # у каждой из них может быть по несколько объектов

        file_name = self.path_json_local + new_class.name + ".json"

        json_dic = {}
        json_dic['name'] = new_class.name
        json_dic['definitions'] = []
        json_dic['objects'] = []
        json_dic['python_file'] = ""
        with open(file_name, 'w') as outfile:
            json.dump(json_dic, outfile, ensure_ascii=False)
        outfile.close()

    def create_object(self, new_obj):
        # по сути все ноды в базе знаний это классы
        # обновление в данном методе объекта (его добавление)
        # так же может быть и добавление кода питона
        # отказался от именования add_node, update_node, read_nide, delete_node
        # т к есть еще взаимодействие не со всем классом, а с его частями
        
        file_name = self.path_json_local + new_obj.name + ".json"


        # открыть файл класса

        # перед записью объектов в json им необходимо id присовоить
        # может быть оставшиеся поля, типа времени

        # создать структуру объекта в json

        # записать в файл


        pass


    def clear_local_files(self):
        local_files = os.listdir(self.path_json_local)
        if local_files:
            os.system("rm " + self.path_json_local + "*")


    def clear_local_links(self):
        pass