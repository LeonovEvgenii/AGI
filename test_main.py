# есть еще библиотека pytest, но я пока не осознал ее необходимость
# необходимо доставлять в отличии от unittest
# pip install pytest
# https://tproger.ru/articles/testiruem-na-python-unittest-i-pytest-instrukcija-dlja-nachinajushhih
# команда на запуск
# python -m unittest test_main.py

import unittest

from scripts.classes.Console import Console


class main_test(unittest.TestCase):
	def test_one_sum(self):

		console = Console()

		a = 2 + 3

		self.assertEqual(a, 5)

	def test_two_sum(self):

		a = 2 + 3
		b = 2 + 2
		c = [a, b]

		self.assertEqual(c, [5, 4])