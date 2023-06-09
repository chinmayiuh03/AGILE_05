# test_program.py

import unittest
from agile import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        result = add(3, 4)
        self.assertEqual(result, 7)

    def test_subtract(self):
        result = subtract(8, 5)
        self.assertEqual(result, 3)

    def test_multiply(self):
        result = multiply(2, 6)
        self.assertEqual(result, 12)

    def test_divide(self):
        result = divide(10, 2)
        self.assertEqual(result, 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()
