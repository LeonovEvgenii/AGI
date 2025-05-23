"""Файл первородной ноды.

Первородная нода возвращает результат выполнения на python.
"""

from scripts.classes.graph.node._Class import _Class


class First_born(_Class):
    """."""

    def __init__(self, word):
        """."""
        super().__init__(word)

        self.path_python_file = ''

    def __str__(self) -> str:
        """Используется при печати графа."""
        return 'первородная: ' + self.name
