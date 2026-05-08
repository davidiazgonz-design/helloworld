import pytest
import unittest
from app.calc import Calculator

@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        # Esta línea es la que te faltaba o estaba mal movida
        self.calc = Calculator()

    def test_divide_by_zero_logic(self):
        """
        Test para cubrir la línea 24 de calc.py (TypeError).
        """
        self.assertRaises(TypeError, self.calc.divide, 10, 0)

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))

    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))

    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)

    def test_multiply_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.multiply(2, 2))

    def test_power_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.power(2, 2))

    def test_substract_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.substract(10, 6))

if __name__ == "__main__":
    unittest.main()
