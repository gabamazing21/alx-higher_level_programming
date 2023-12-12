import unittest
from models.rectangle import Rectangle
class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(8, 4, 2, 3, 1)

    def test_get_width(self):
        self.assertEqual(self.rectangle.width, 8)

    def test_get_height(self):
        self.assertEqual(self.rectangle.height, 4)

    def test_get_x(self):
        self.assertEqual(self.rectangle.x, 2)

    def test_get_y(self):
        self.assertEqual(self.rectangle.y, 3)

    def test_set_width(self):
        self.rectangle.width = 2
        self.assertEqual(self.rectangle.width, 2)
    def test_set_height(self):
        self.rectangle.height = 3
        self.assertEqual(self.rectangle.height, 3)
    def test_set_x(self):
        self.rectangle.x = 5
        self.assertEqual(self.rectangle.x, 5)
    def test_set_y(self):
        self.rectangle.y = 7
        self.assertEqual(self.rectangle.y, 7)
