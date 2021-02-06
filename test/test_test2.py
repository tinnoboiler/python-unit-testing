from . import Test
from test2 import find_longest

def test_find_longest(): 
    Test.assertEqual(find_longest("The quick white fox jumped around the massive dog"), 7)
    Test.assertEqual(find_longest("Take me to tinseltown with you"), 10)
    Test.assertEqual(find_longest("Sausage chops"), 7)
    Test.assertEqual(find_longest("Wind your body and wiggle your belly"), 6)
    Test.assertEqual(find_longest("Lets all go on holiday"), 7)