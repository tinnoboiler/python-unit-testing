import unittest
from unittest.mock import patch
from app.test4 import compute

class Test4(unittest.TestCase):

    @classmethod
    def setUpClass(self):        
        patch('app.test4.expensive_api_call', return_value=123).start()
    
    @unittest.skip('skip real api call test')
    def test_compute(self):
        expected = 124
        actual = compute(1)
        self.assertEqual(expected, actual)
    
    def test_mock_compute(self):
        expected = 124        
        actual = compute(1)
        self.assertEqual(expected, actual)
