import unittest

import pandas as pd

from mfreport.yfwrapper import Yfwrapper


class TestYfwrapper(unittest.TestCase):
    def test_init(self):
        units = pd.Series(data=[1, 1], index=["9984.T", "V"])
        df = Yfwrapper(units).get_info()

        self.assertEqual("Visa", df.at["V", "shortName"])
        self.assertGreater(df.at["V", "divTotal"], 100.0)
        self.assertGreater(df.at["V", "divAug"], 10.0)
        self.assertEqual(df.at["V", "divDec"], 0.0)
