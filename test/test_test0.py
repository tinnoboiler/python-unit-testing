from . import Test
from test0 import multiply

def test_multiply():        
    Test.assertEqual(multiply(2, 3), 6, "2 * 3 should return 6")
    Test.assertEqual(multiply(4, 5), 20, "4 * 5 should return 20")    