import unittest

from mfreport.main import msg


class TestMsg(unittest.TestCase):
    def test_msg(self):
        self.assertEqual(msg(), "Hello, world!")
