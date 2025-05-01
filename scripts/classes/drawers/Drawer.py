"""Общий класс для всех рисовалок."""

from abc import ABC, abstractmethod

from scripts.classes.Graph import Graph


class Drawer(ABC):
    """Абстрактный класс рисователь."""

    @abstractmethod
    def draw(self, graph: Graph):
        """Метод для рисования графа."""
        pass
