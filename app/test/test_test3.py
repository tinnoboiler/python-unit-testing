from unittest import TestCase
from app.test3 import order


class Test3(TestCase):
    
    def test_order(self):        
        self.assertEqual(order("is2 This1 Test4 a3"), "This1 is2 a3 Test4")
        self.assertEqual(order("of4 For1 people6 good3 the5 the2"), "For1 the2 good3 of4 the5 people6")
        self.assertEqual(order(""), "")
    