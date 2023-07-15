import unittest
from models.rectangle import Rectangle
"""test module for rectangle"""


class TestRectangle(unittest.TestCase):
    """Rectangle class"""

    def test_rectangle(self):
        try:
            Rectangle(10, "2")
        except Exception as e:
            self.assertEqual(str(e), "height must be an integer")
        try:
            Rectangle("10", 2)
        except Exception as e:
            self.assertEqual(str(e), "width must be an integer")
        try:
            Rectangle(10, 2, "3")
        except Exception as e:
            self.assertEqual(str(e), "x must be an integer")
        try:
            Rectangle(10, 2, 3, "7")
        except Exception as e:
            self.assertEqual(str(e), "y must be an integer")
        try:
            Rectangle(10, -2)
        except Exception as e:
            self.assertEqual(str(e), "height must be > 0")
        try:
            r = Rectangle(10, 2)
            r.width = -1
        except Exception as e:
            self.assertEqual(str(e), "width must be > 0")
        try:
            Rectangle(10, 2, 3, -1)
        except Exception as e:
            self.assertEqual(str(e), "y must be >= 0")
        try:
            Rectangle(10, 2, -3, 1)
        except Exception as e:
            self.assertEqual(str(e), "x must be >= 0")
    
    def test_area(self):
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)


    
