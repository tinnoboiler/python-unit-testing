import unittest
from unittest.mock import patch
from app.test6 import compute

# smart mock function
def smart_compute(x):
    return x * 2

class Test6(unittest.TestCase):

    def test_compute(self):
        expected = 12
        actual = compute(6)
        self.assertEqual(expected, actual)
