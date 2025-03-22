from abc import ABC, abstractmethod
from scripts.classes.Graph import Graph


class Drawer(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def draw(self, graph: Graph):
        pass
