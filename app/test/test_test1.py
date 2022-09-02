from unittest import TestCase
from app.test1 import spin_words


class Test1(TestCase):

    def test_spin_words(self):
        # start by writing assert test below
        self.assertEqual(
            spin_words("Hey fellow warriors"), "Hey wollef sroirraw")
        self.assertEqual(spin_words("This is a test"), "This is a test")
        self.assertEqual(
            spin_words("This is another test"), "This is rehtona test")
