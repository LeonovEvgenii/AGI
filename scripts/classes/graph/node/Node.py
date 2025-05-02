"""Файл вершины графа."""

# будут ли другие типы нод, например датчик?


class Node():
    """."""

    def __init__(self, name):
        """."""
        self.name = name

    def return_name_for_draw(self):
        """."""
        pass

    def __str__(self):
        """Используется при печати графа."""
        return 'нода: ' + self.name
