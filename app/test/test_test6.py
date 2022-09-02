import unittest
from unittest.mock import patch
from app.test6 import compute


# smart mock function
def smart_compute(x):
    return x * 2


class Test6(unittest.TestCase):

    # patch the expensive api call with a mock function
    @patch('app.test6.expensive_smart_api_call', smart_compute)
    def test_mock_compute(self):
        expected = 12
        actual = compute(6)
        self.assertEqual(expected, actual, f"should return value {expected}")
