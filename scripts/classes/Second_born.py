from scripts.classes._Class import _Class
from scripts.classes.Graph import Graph

class Second_born(_Class):

    def __init__(self, word):
        super().__init__(word)

        self.definition = Graph()