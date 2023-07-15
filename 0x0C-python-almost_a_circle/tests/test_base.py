import unittest
from models.base import Base
"""test module for base"""


class TestBase(unittest.TestCase):
    """class for test base"""


    def test_base(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(100)
        self.assertEqual(b3.id, 100)
        b4 = Base(None)
        self.assertEqual(b4.id, 3)
