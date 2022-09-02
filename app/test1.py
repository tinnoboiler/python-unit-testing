"""
Write a function that takes in a string of one or more words,
and returns the same string, but with all five or more letter words reversed.
Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.

Examples:
spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
spinWords( "This is a test") => returns "This is a test"
spinWords( "This is another test" )=> returns "This is rehtona test"

Before you begin, complete its unit test case under the test directory.
"""


def spin_words(sentence):
    new_sentence = []
    # start coding below
    sentence.split()
    for word in sentence.split():
        if len(word) >= 5:
            word = word[::-1]
        new_sentence.append(word)
    return ' '.join(new_sentence)
