from . import Test
from test4 import get_sum

def test_get_sum():        
    Test.assertEqual(get_sum(0,1),1)
    Test.assertEqual(get_sum(1,2),3)
    Test.assertEqual(get_sum(1,1),1)
    Test.assertEqual(get_sum(0,-1),-1)
    Test.assertEqual(get_sum(-1, 2),2)    