# есть еще библиотека pytest, но я пока не осознал ее необходимость
# необходимо доставлять в отличии от unittest
# pip install pytest
# https://tproger.ru/articles/testiruem-na-python-unittest-i-pytest-instrukcija-dlja-nachinajushhih
# команда на запуск
# python -m unittest test_main.py

import unittest

from scripts.classes.Console import Console
from scripts.classes.drawers.Xdot import Xdot
from scripts.classes.Core import Core


class Main_test(unittest.TestCase):

    def test_console(self):

        # print("\nТест модуля консоль.")
        # print("На вход подается текст предложения, преобразуется в граф и обратно из графа в текст.")

        console = Console()

        input_graphs = console.content_to_graphs("1 2 3 4. 5 6 7 8.")

        # for graph in input_graphs:
        #     print(graph)

        output_text = console.graphs_to_content(input_graphs)

        self.assertEqual(output_text, "1 2 3 4. 5 6 7 8.")

    def test_draw(self):

        # print("\nТест модуля рисователь.")
        # print("На вход подаются графы, рисуются, с различными опциями.")

        console = Console()

        input_graphs = console.content_to_graphs("1 2 3 4. 5 6 7 8.")

        xdot = Xdot()

        # далее требуется рисование именно нескольких графов
        xdot.draw(input_graphs)

    def test_first_born(self):
        pass

    def test_second_born(self):
        pass

    def test_set_definition(self):
        pass

    def test_get_definition(self):
        pass

    def test_compare_definition(self):
        pass

    def test_one_dialog(self):
        pass

    def test_numeric(self):
        pass

    # def test_one_sum(self):

    # 	console = Console()
    # 	drawer = Drawer()
    # 	core = Core()

    # 	input_graph = console.content_to_graph("2 + 3")

    # 	print(input_graph)

    # 	output_graph = core.run_nodes_2(input_graph)

    # 	# console.graph_to_content(output_graph, print=True) # если печатать в консоль (не для теста)
    # 	output_text = console.graph_to_content(output_graph)

    # 	self.assertEqual(output_text, "5")

    # def test_two_sum(self):

    # 	a = 2 + 3
    # 	b = 2 + 2
    # 	c = [a, b]

    # 	self.assertEqual(c, [5, 4])


if __name__ == "__main__":
    mt = Main_test()

    # вызывать методы по отдельности нужно, только если запуск осуществляется через голый python
    # без указания модуля unittest (python3 test_main.py).
    # При запуске через unittest "python -m unittest test_main.py" код вызова отдельных методов
    # не учитывается.
    mt.test_console()
