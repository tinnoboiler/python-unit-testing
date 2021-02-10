from unittest import TestCase
from app.test1 import get_count


class Test1(TestCase):
    
    def test_get_count(self):        
        self.assertEqual(get_count("abracadabra"), 5)
        self.assertEqual(get_count("xesdac"), 2)
    