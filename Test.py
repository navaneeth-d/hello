#!/usr/bin/env python3


import unittest

from Prog1 import summation

class TestSum(unittest.TestCase):
    def test_sum(self):
        data = [1, 2, 3, 4, 5]
        result = summation(data)
        self.assertEqual(result, 15)
