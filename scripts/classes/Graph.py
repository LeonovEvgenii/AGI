from scripts.classes.Link import Link
from scripts.classes.First_born import First_born
from scripts.classes.Second_born import Second_born
from scripts.classes._Object import _Object


class Graph():

    def __init__(self, name=""):
        self.name = name

        self.classes = []
        self.objects = []
        
        self.nodes = []
        self.links = []

    # def add_node(self, node_obj):
    #     self.nodes.append(node_obj)
        
    def return_class(self, word):
        for c_class in self.classes:
            if c_class.name == word:
                return c_class
            
        return False

    def add_node(self, word, number_in_sentence):

        # проверка на класс
        #     если нет, создаем класс
        #         внутри класса первый объект
        #     если да
        #         добавляем в объект


        c_class = self.return_class(word)

        if c_class == False:
            # создаем класс
            self.classes.append(First_born(word))
            # перый объект внутри класса автоматически не создается
        else:
            # добавляем в объект

            # в параметры создания объекта передается только имя класса
            # сам _Object создается не внутри _Class, а снаружи
            # для добавления в спсок всех объектов в клссе Graph.
            # Мог бы и внутри _Class создаваться, но тогда его возвращать надо в Graph

            # это кстати идея
            # сделать автоматическое создание одного объекта при создании класса
            # сделать метод возврата всех объетов
            # в классе граф при актуализации всех нод идет добавление класса и вытаскивание из него всех объектов
            # раньше кстати так и было, создавался и класс и объект

            new_object = _Object(c_class.name, number_in_sentence)
            c_class.add_obj(new_object)
            self.objects.append(new_object)

        self.merge_list_nodes()


    def merge_list_nodes(self):
        self.nodes = self.classes + self.objects

    def __str__(self):
        rez_str = ""
        for node in self.nodes:
            rez_str += node.name + node.get_type()
            rez_str += " "

        if rez_str:
            return 'Список вершин графа "' + self.name + '" :' + rez_str
        else:
            return "граф пустой"


