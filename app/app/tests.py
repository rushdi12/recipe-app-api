"""
sample tests
"""

from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module """

    def test_add_numbers(self):
        """test adding numbers together """
        res = calc.add(5, 4)

        self.assertEqual(res, 9)

    def test_subtract_number(self):
        """test subtracting numbers """
        res = calc.subtract(15, 10)

        self.assertEqual(res, 5)
