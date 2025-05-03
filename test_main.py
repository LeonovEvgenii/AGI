"""unit тесты проекта."""

# есть еще библиотека pytest, но я пока не осознал ее необходимость
# необходимо доставлять в отличии от unittest
# pip install pytest
# https://tproger.ru/articles/testiruem-na-python-unittest-i-pytest-instrukcija-dlja-nachinajushhih
# команда на запуск
# python -m unittest test_main.py

import os
import unittest

from scripts.classes.conversion.Console import Console
from scripts.classes.drawers.Xdot import Xdot


class Main_test(unittest.TestCase):
    """Основной класс для работы тестов."""

    def test_console(self):
        """Тест модуля консоль.

        На вход подается текст предложения, преобразуется в граф и
        обратно из графа в текст.
        """
        console = Console()

        input_graphs = console.content_to_graphs('1 2 3 4. 5 6 7 8.')

        # for graph in input_graphs:
        #     print(graph)

        output_text = console.graphs_to_content(input_graphs)

        # у этого метода есть третий параметр, печать строки, если тест не
        # прошел
        self.assertEqual(output_text, '1 2 3 4. 5 6 7 8.')

    def test_draw(self):
        """Тест модуля рисователь.

        На вход подаются графы, рисуются, с различными опциями.
        """
        console = Console()

        input_graphs = console.content_to_graphs('1 2 3 4. 5 6 7 8.')

        xdot = Xdot()

        path = 'test_xdot.dot'

        xdot.draw(input_graphs, path=path)

        with open(path, 'r') as f:
            file_content = f.read()

        sample = """strict graph G {
"первородная: 1" -- "объект: 1 id: 0"
"первородная: 2" -- "объект: 2 id: 0"
"объект: 1 id: 0" -- "объект: 2 id: 0"
"первородная: 3" -- "объект: 3 id: 0"
"объект: 2 id: 0" -- "объект: 3 id: 0"
"первородная: 4" -- "объект: 4 id: 0"
"объект: 3 id: 0" -- "объект: 4 id: 0"
"первородная: 5" -- "объект: 5 id: 0"
"первородная: 6" -- "объект: 6 id: 0"
"объект: 5 id: 0" -- "объект: 6 id: 0"
"первородная: 7" -- "объект: 7 id: 0"
"объект: 6 id: 0" -- "объект: 7 id: 0"
"первородная: 8" -- "объект: 8 id: 0"
"объект: 7 id: 0" -- "объект: 8 id: 0"
}
"""
        self.assertEqual(file_content, sample)

        if os.path.exists(path):
            os.remove(path)
        else:
            print(f'Файл {path} не найден')

    def test_first_born(self):
        """Тест первородной ноды."""
        console = Console()

        input_graphs = console.content_to_graphs('время')

        for node in input_graphs[0].nodes:
            if node.__class__.__name__ == 'First_born':
                node.path_python_file = 'knowledge_base/python_program/time.py'

        # for graph in input_graphs:
        #     print(graph)

    def test_second_born(self):
        """Тест второродной ноды."""
        pass

    def test_set_definition(self):
        """Тест задания определения ноды."""
        pass

    def test_get_definition(self):
        """Тест получения определения ноды."""
        pass

    def test_compare_definition(self):
        """Тест сравнения определений."""
        pass

    def test_one_dialog(self):
        """Тест диалога."""
        pass

    def test_numeric(self):
        """Тест предметной области цифры."""
        pass

    # def test_one_sum(self):

    # 	console = Console()
    # 	drawer = Drawer()
    # 	core = Core()

    # 	input_graph = console.content_to_graph("2 + 3")

    # 	print(input_graph)

    # 	output_graph = core.run_nodes_2(input_graph)

    #   # если печатать в консоль (не для теста)
    # 	# console.graph_to_content(output_graph, print=True)
    # 	output_text = console.graph_to_content(output_graph)

    # 	self.assertEqual(output_text, "5")

    # def test_two_sum(self):

    # 	a = 2 + 3
    # 	b = 2 + 2
    # 	c = [a, b]

    # 	self.assertEqual(c, [5, 4])


if __name__ == '__main__':
    mt = Main_test()

    # вызывать методы по отдельности нужно, только если запуск осуществляется
    # через голый python без указания модуля unittest (python3 test_main.py).
    # При запуске через unittest "python -m unittest test_main.py" код вызова
    # отдельных методов не учитывается.
    mt.test_console()
