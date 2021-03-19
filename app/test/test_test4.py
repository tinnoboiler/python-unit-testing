import unittest
from unittest.mock import patch
from app.test4 import compute

class Test4(unittest.TestCase):

    def test_compute(self):
        expected = 124
        actual = compute(1)
        self.assertEqual(expected, actual)
    
