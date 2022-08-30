import unittest

from mfreport.yfwrapper import Yfwrapper


class TestYfwrapper(unittest.TestCase):
    def test_init(self):
        df = Yfwrapper(["9984.T", "V"]).get_info()

        self.assertEqual("Visa Inc.", df.at["V", "shortName"])
        self.assertGreater(df.at["V", "divTotal"], 100.0)
        self.assertGreater(df.at["V", "divAug"], 10.0)
        self.assertEqual(df.at["V", "divDec"], 0.0)
