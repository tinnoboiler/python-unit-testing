import unittest
from unittest.mock import patch
from app.test5 import compute

class Test5(unittest.TestCase):

    def test_compute(self):
        expected = 124
        actual = compute(1)
        self.assertEqual(expected, actual)
