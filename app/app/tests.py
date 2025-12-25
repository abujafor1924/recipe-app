from django.test import SimpleTestCase
from app import calc

class SimpleTest(SimpleTestCase):
     def test_add_numbers(self):
          """Test adding two numbers together."""
          res = calc.add(5, 6)
          self.assertEqual(res, 11)
# end class
     def test_subtract_numbers(self):
          """Test subtracting two numbers."""
          res = calc.subtract(10, 14)
          self.assertEqual(res, -4)