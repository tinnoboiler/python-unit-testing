import unittest
from app.test5 import compute
from unittest.mock import patch


class Test5(unittest.TestCase):

    def test_compute(self):
        expected = 12
        actual = compute(6)
        self.assertEqual(expected, actual)
