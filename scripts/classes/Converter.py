"""Общий класс для всех конвертеров данных в граф и наоборот."""

from abc import ABC, abstractmethod


class Converter(ABC):
    """Класс конвертера."""

    def __init__(self):
        """Конструктор конвертера."""
        # Сначала хотел создать два касса конверторов:
        # один для преобразования контента в граф,
        # другой, наоборот, из графа в контент.
        # Но, т к они могут работать с общими библиотеками,
        # решил оставить в одном классе.
        self.output_content = None
        self.input_content = None

        # используется для преобразования контента в граф
        self.output_graphs = None

        # используется для преобразования графа в контент
        self.input_graphs = None

        # input_content -> output_graphs
        # input_graphs -> output_content

    @abstractmethod
    def content_to_graphs(self):
        """Обязательные методы ради которых создавался конвертер."""
        pass

    @abstractmethod
    def graphs_to_content(self):
        """Обязательные методы ради которых создавался конвертер."""
        pass

    # Возможно добавление методов для фильтрации
    # Слово filter зарезервировано в python
