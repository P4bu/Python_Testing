# python -m unittest discover -v -s tests
import unittest

from src.calculator import sum, subtract, multiple, divide

class CalculatorTests(unittest.TestCase):

    def test_sum(self):
        assert sum(2, 3) == 5

    def test_subtract(self):
        assert subtract(10, 5) == 5

    def test_multiple(self):
        assert multiple(2, 3) == 6        

    def test_divide(self):
        assert divide(4, 2) == 2    

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(3, 0)    