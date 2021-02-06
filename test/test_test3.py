from . import Test
from test3 import order

def test_order():        
    Test.assertEqual(order("is2 This1 Test4 a3"), "This1 is2 a3 Test4")
    Test.assertEqual(order("of4 For1 people6 good3 the5 the2"), "For1 the2 good3 of4 the5 people6")
    Test.assertEqual(order(""), "")
    