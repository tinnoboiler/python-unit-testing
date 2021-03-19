'''
Your task is to sort a given string. Each word in the string will end with a single number. 

This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

Examples:
    "is2 This1 Test5 a3"  -->  "This1 is2 a3 Test4"
    "of4 For1 people6 good3 the5 the2"  -->  "For1 the2 good3 of4 the5 people6"
    ""  -->  ""
'''

def order(sentence: str)->str:
  # code here. hint: you may use split, string[-1] and join    

  return