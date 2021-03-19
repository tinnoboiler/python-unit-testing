import unittest
from unittest.mock import patch
from app.test5 import compute

# smart mock function
def smart_compute(x):
    return x * 2

class Test4(unittest.TestCase):
    
    def test_compute(self):
        expected = 12
        actual = compute(6)
        self.assertEqual(expected, actual)