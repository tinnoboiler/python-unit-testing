import unittest
from unittest.mock import patch
from app.test5 import compute

# smart mock function
def smart_compute(x):
    return x * 2

class Test5(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # replace actual api call with a mock function
        patch('app.test5.expensive_smart_api_call', side_effect=smart_compute).start()

    def test_compute(self):
        expected = 12
        actual = compute(6)
        self.assertEqual(expected, actual)

    def test_mock_compute(self):
        """ Same mock effect as above,
        except mocking scope is reduced to this method"""
        expected = 12
        with patch('app.test5.expensive_smart_api_call', side_effect=smart_compute):
            actual = compute(6)
        self.assertEqual(expected, actual, f"should return value {expected}")

    @classmethod
    def tearDownClass(self):
        # clear the resources when test is done
        pass
