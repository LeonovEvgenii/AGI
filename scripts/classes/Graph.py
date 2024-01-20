from scripts.classes.Link import Link
from scripts.classes.First_born import First_born
from scripts.classes.Second_born import Second_born


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
            c_class.add_obj(number_in_sentence)

        self.merge_list_nodes()


    def merge_list_nodes(self):
        self.nodes = self.classes + self.objects





    def __str__(self):
        rez_str = ""
        for node in self.nodes:
            rez_str += node.__str__()
            rez_str += " "

        if rez_str:
            return 'Список вершин графа "' + self.name + '" :' + rez_str
        else:
            return "граф пустой"

    def save_nodes_from_graph(self, graph):
        
        return

        for node in graph.nodes:
            if node not in self.nodes:
                self.nodes.append(node)
            else:
                # сравнить две ноды по определениям
                pass

