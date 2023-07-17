import unittest
from models.rectangle import Rectangle
from models.base import Base
"""test module for rectangle"""


class TestRectangle(unittest.TestCase):
    """Rectangle class"""

    def test_rectangle(self):
        Base._Base__nb_objects = 0
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")
        r2.width = 3
        self.assertEqual(r2.width, 3)
        try:
            r4 = Rectangle(5)
        except Exception as e:
            self.assertEqual(str(e), "__init__() missing 1 required positional argument: 'height'")
        try:
            r4 = Rectangle()
        except Exception as e:
            self.assertEqual(str(e), "__init__() missing 2 required positional arguments: 'width' and 'height'")
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
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

    
    def test_area(self):
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)


    def test_Display(self):
        str_out = "  ##\n  ##\n  ##"


if __name__ == '__main__':
    unittest.main()
