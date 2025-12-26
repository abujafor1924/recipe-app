from django.test import SimpleTestCase
from app import calc


class SimpleTest(SimpleTestCase):
    def test_add_numbers(self):
        """Test adding two numbers together."""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test subtracting two numbers."""
        res = calc.sub(10, 14)
        self.assertEqual(res, -4)
