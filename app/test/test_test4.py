import unittest
from unittest.mock import patch
from app.test4 import compute

class Test4(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # mock the function for entire test suite
        patch('app.test4.expensive_api_call', return_value=123).start()

    def test_compute(self):
        expected = 124
        actual = compute(1)
        self.assertEqual(expected, actual)

    def test_mock_compute(self):
        """ Same mock effect as above,
        except mocking scope is reduced to this method"""
        expected = 124
        with patch('app.test4.expensive_api_call', return_value=123):
            actual = compute(1)
        self.assertEqual(expected, actual)

    @classmethod
    def tearDownClass(self):
        # clear the resources when test is done
        pass
