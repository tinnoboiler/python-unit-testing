from unittest import TestCase
from app.test2 import find_longest


class Test2(TestCase):

    def test_find_longest(self):
        self.assertEqual(find_longest("The quick white fox jumped around the massive dog"), 7)
        self.assertEqual(find_longest("Take me to tinseltown with you"), 10)
        self.assertEqual(find_longest("Sausage chops"), 7)
        self.assertEqual(find_longest("Wind your body and wiggle your belly"), 6)
        self.assertEqual(find_longest("Lets all go on holiday"), 7)