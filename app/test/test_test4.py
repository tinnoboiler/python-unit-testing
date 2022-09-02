from unittest import TestCase
from app.test4 import order


<<<<<<< HEAD
    def test_compute(self):
        expected = 124
        actual = compute(1)
        self.assertEqual(expected, actual)
    
=======
class Test4(TestCase):

    def test_order(self):
        # start by writing assert test below
        self.assertEqual(order("is2 This1 Test4 a3"), "This1 is2 a3 Test4")
        self.assertEqual(
            order("of4 For1 people6 good3 the5 the2"),
            "For1 the2 good3 of4 the5 people6"
        )
        self.assertEqual(order(""), "")
>>>>>>> answer
