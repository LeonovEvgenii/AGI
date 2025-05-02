"""Файл второродной вершины.

В своем определении содержат другие вершины.
"""

from scripts.classes.graph.node._Class import _Class
# не могу использовать из-за циклического импорта
# from scripts.classes.graph.Graph import Graph


class Second_born(_Class):
    """."""

    def __init__(self, word, definition=None):
        """."""
        super().__init__(word)

        # не могу в конструкторе писать self.definition = Graph()
        # иначе будет циклический импорт с файлом Graph
        self.definition = definition

    # такая функция невозможна из-за циклического импорта
    # def create_def(self, list_nodes):
    #     self.g = Graph()

    def __str__(self) -> str:
        """Используется при печати графа."""
        return 'второродная: ' + self.name
