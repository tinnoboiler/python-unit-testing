from unittest import TestCase
from app.test2 import get_count


class Test2(TestCase):

    def test_get_count(self):
        # start by writing assert test below
        self.assertEqual(get_count("abracadabra"), 5)
        self.assertEqual(get_count("xesdac"), 2)
