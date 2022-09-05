import unittest

from mfreport.client import example_html
from mfreport.parser import Parser


class TestParse(unittest.TestCase):
    def test_parse(self):
        p = Parser(example_html)
        df = p.get_stock()
        self.assertEqual(30, df.at["IBM", "units"])
        self.assertEqual(100000, df.at["7203.T", "price"])
