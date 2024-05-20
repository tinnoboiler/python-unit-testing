import unittest
from unittest.mock import patch
from app.test5 import compute


class Test5(unittest.TestCase):

    def test_mock_compute(self):
        # use patch or mock the expensive api function
        expected = 124
        actual = compute(1)
        self.assertEqual(expected, actual)