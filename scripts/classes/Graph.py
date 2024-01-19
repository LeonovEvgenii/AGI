from scripts.classes.Link import Link
from scripts.classes.First_born import First_born
from scripts.classes.Second_born import Second_born


class Graph():

    def __init__(self, name=""):
        self.name = name
        self.nodes = []
        self.links = []

    def add_node(self, node_obj):
        self.nodes.append(node_obj)

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
        
        for node in graph.nodes:
            if node not in self.nodes:
                self.nodes.append(node)
            else:
                # сравнить две ноды по определениям
                pass

