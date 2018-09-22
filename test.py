import unittest

import calc

class TestCalc(unittest.TestCase):

    def test_addition(self):
        result1 = calc.add(2, 3)
        self.assertEqual(5, result1)