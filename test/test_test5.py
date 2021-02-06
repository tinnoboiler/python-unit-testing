from . import Test
from test5 import high

def test_high():            
    Test.assertEqual(high('man i need a taxi up to ubud'), 'taxi')
    Test.assertEqual(high('what time are we climbing up the volcano'), 'volcano')
    Test.assertEqual(high('take me to semynak'), 'semynak')
