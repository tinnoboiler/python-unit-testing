"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, and u as vowels.

The input string will only consist of lower case letters and/or spaces.
e.g. 
get_count('xesdac') -> 2
get_count("abracadabra") -> 5
"""

def get_count(inputStr: str)->int:
    num_vowels = 0
    # your code here. hint:you may use 'for', 'in' and 'sum'
    for char in inputStr:
        if char in ['a', 'e', 'i', 'o', 'u']:
            num_vowels += 1            
    return num_vowels    
