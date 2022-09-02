from unittest import TestCase
from app.test0 import multiply


class Test0(TestCase):

    def test_multiply(self):
        # start by writing assert test below
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(3, 3), 9)
        self.assertEqual(multiply(4, 4), 16)
