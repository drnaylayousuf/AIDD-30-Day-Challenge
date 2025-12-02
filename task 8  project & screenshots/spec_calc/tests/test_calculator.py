# tests/test_calculator.py

import unittest
import sys
import io
from unittest.mock import patch

from src.calculator import add, subtract, multiply, divide
from src.__main__ import main # Import main from __main__.py

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(2, 5), -3)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 5), -5)
        self.assertEqual(multiply(0, 10), 0)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(-10, 2), -5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_operator_main(self, mock_stdout):
        with patch('sys.argv', ['__main__.py', '10', 'x', '2']):
            main()
            self.assertIn("Error: Unsupported operator 'x'", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_operand_main(self, mock_stdout):
        with patch('sys.argv', ['__main__.py', 'abc', '+', '2']):
            with self.assertRaises(SystemExit): # argparse exits on type conversion error
                main()
            # Error message for invalid float conversion is handled by argparse and printed to stderr by default
            # We are checking for SystemExit as an indicator of invalid input handling by argparse
            # For more detailed checks, stderr would need to be captured, but SystemExit is sufficient here

if __name__ == '__main__':
    unittest.main()
