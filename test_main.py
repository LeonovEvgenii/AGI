# есть еще библиотека pytest, но я пока не осознал ее необходимость
# необходимо доставлять в отличии от unittest
# pip install pytest
# https://tproger.ru/articles/testiruem-na-python-unittest-i-pytest-instrukcija-dlja-nachinajushhih
# команда на запуск
# python -m unittest test_main.py

import unittest

from scripts.classes.Console import Console
from scripts.classes.Drawer import Drawer
from scripts.classes.Core import Core

class Main_test(unittest.TestCase):
	def test_console(self):

		console = Console()

		input_graph = console.content_to_graph("1 2 3 4")

		output_text = console.graph_to_content(input_graph)

		self.assertEqual(output_text, "1 2 3 4")
	
	
	def test_one_sum(self):

		console = Console()
		drawer = Drawer()
		core = Core()

		input_graph = console.content_to_graph("2 + 3")

		print(input_graph)

		output_graph = core.run_nodes_2(input_graph)

		# console.graph_to_content(output_graph, print=True) # если печатать в консоль (не для теста)
		output_text = console.graph_to_content(output_graph)

		self.assertEqual(output_text, "5")

	def test_two_sum(self):

		a = 2 + 3
		b = 2 + 2
		c = [a, b]

		self.assertEqual(c, [5, 4])

if __name__ =="__main__":
	mt = Main_test()
	mt.test_console()