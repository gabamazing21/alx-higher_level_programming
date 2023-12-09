#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer
class TestMax(unittest.TestCase):
    def test_max_integer(self):
        result = max_integer([1, 2, 3, 4, 10, 15, 2, 4])
        self.assertEqual(15, result)
        self.assertEqual(max_integer([10,4,6,6,3,3]), 10)
        self.assertEqual(max_integer([0,4,8,15,6,3,3]), 15)
        self.assertEqual(max_integer([10,4,6,6,3,3,20]), 20)
        self.assertEqual(max_integer([-5,-3,-2,-1]), -1)
        self.assertEqual(max_integer([10]), 10)
        self.assertEqual(max_integer([]), None)





