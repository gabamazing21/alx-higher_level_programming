import unittest
from models.rectangle import Rectangle
class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(8, 4, 2, 3, 1)

    def test_get_width(self):
        self.assertEqual(self.rectangle.getWidth(), 8)

    def test_get_height(self):
        self.assertEqual(self.rectangle.getHeight(), 4)

    def test_get_x(self):
        self.assertEqual(self.rectangle.getX(), 2)

    def test_get_y(self):
        self.assertEqual(self.rectangle.getY(), 3)

    def test_set_width(self):
        self.rectangle.setWidth(2),
        self.assertEqual(self.rectangle.getWidth(), 2)
    def test_set_height(self):
        self.rectangle.setHeight(3),
        self.assertEqual(self.rectangle.getHeight(), 3)
    def test_set_x(self):
        self.rectangle.setX(5),
        self.assertEqual(self.rectangle.getX(), 5)
    def test_set_y(self):
        self.rectangle.setY(7),
        self.assertEqual(self.rectangle.getY(), 7)
