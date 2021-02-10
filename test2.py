"""
Find and return the length of the longest word, as a number.

There will only be one 'longest' word.

e.g. find_longest("Lets all go on holiday") --> 7
"""

def find_longest(sentence: str)->int:        
    # code here. hint: you may use 'split' and 'len'   
    longest = 0
    for word in sentence.split():
        if len(word) > longest:
            longest = len(word)
    return longest