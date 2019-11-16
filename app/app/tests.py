from django.test import TestCase

from app.calc import add, substract


class CalcTest(TestCase):

    def test_add_numbers(self):
        """Test that two number are added together"""
        self.assertEqual(add(3, 8), 11)

    def test_sub_numbers(self):
        """Test that values are substracgted and returned"""
        self.assertEqual(substract(5, 11), 6)
