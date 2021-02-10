from unittest import TestCase
from app.test0 import spin_words


class Test0(TestCase):
    
    def test_spin_words(self):         
        self.assertEqual(spin_words("Hey fellow warriors"), "Hey wollef sroirraw")
        self.assertEqual(spin_words("This is a test"), "This is a test")
        self.assertEqual(spin_words("This is another test"), "This is rehtona test")