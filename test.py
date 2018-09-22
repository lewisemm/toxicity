import unittest

import calc

class TestCalc(unittest.TestCase):

    def test_addition(self):
        result = calc.add(2, 3)
        self.assertEqual(5, result)

    def test_subtraction(self):
        result = calc.subtract(2, 3)
        self.assertEqual(-1, result)

    def test_multiplication(self):
        result = calc.multiply(2, 3)
        self.assertEqual(6, result)

    def test_division(self):
        result = calc.divide(2, 3)
        self.assertEqual(0.667, round(result, 3))