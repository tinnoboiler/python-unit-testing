import unittest
from unittest.mock import patch
from app.test5 import compute


class Test5(unittest.TestCase):

    def test_mock_compute(self):
        expected = 124
        with patch('app.test5.expensive_api_call', return_value=123):
            actual = compute(1)
        self.assertEqual(expected, actual)
