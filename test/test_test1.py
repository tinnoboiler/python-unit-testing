from . import Test
from test1 import get_count

def test_get_count():        
    Test.assertEqual(get_count("abracadabra"), 5)    
    Test.assertEqual(get_count("xesdac"), 2)    
    