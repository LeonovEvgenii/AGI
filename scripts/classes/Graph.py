from scripts.classes.Link import Link
from scripts.classes.First_born import First_born

# операции по созданию нод выносим вне класса, т к в Second_born уже есть импорт Graph
# from scripts.classes.Second_born import Second_born
# можно одновременно и в  Graph и в Second_born не импротрировать ни Graph ни Second_born
# ну или решить, где главнее ( в графе)


class Graph():

    def __init__(self):
        self.nodes = []
        self.links = []

    def add_node(self, node_obj):
        self.nodes.append(node_obj)



