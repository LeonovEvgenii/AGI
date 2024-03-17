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

class main_test(unittest.TestCase):
	def test_one_sum(self):

		console = Console()
		drawer = Drawer()
		core = Core()

		input_graph = console.paste_input_data("2 + 3")

		print(input_graph)

		a = 2 + 3

		self.assertEqual(a, 5)

	def test_two_sum(self):

		a = 2 + 3
		b = 2 + 2
		c = [a, b]

		self.assertEqual(c, [5, 4])