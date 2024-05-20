import unittest
from unittest.mock import patch
from app.test6 import compute


# smart mock function that can return same result
def smart_compute(x):
    return x


class Test6(unittest.TestCase):

    def test_mock_compute(self):
        # use above smart function to simulate the api call
        expected = 12
        actual = compute(6)
        self.assertEqual(expected, actual, f"should return value {expected}")
