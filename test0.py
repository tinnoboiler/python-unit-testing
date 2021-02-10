"""
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed. 
Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") => returns "This is a test" spinWords( "This is another test" )=> returns "This is rehtona test"
"""

""" Easiest but long code to solve the problem """
# def spin_words(sentence):
#     words = sentence.split()
#     new_sentence = ""
#     for word in words:
#         if len(word) >= 5:
#             new_sentence += f" {word[::-1]}"
#         else:
#             new_sentence += f" {word}"
#     return new_sentence.strip()

""" Refactored code: good balance of conciseness and readability """
def spin_words(sentence):
    new_sentence = []
    for word in sentence.split():
        new_sentence.append(word[::-1] if len(word) >= 5 else word)        
    return " ".join(new_sentence)

""" Bad code: hard to read and maintain """
# def spin_words(sentence):
#     return " ".join([ word[::-1] if len(word) >= 5 else word for word in sentence.split() ])    