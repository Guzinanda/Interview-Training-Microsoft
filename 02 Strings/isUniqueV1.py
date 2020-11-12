
def cleanStr(word):
    # Lower case the word:
    cleaned_word = word.lower()

    # Eliminate blank spaces:
    cleaned_word = word.replace(" ", "")

    return cleaned_word


def isUnique(word):

    # "Hello World" -> "helloworld"
    cleaned_word = cleanStr(word)

    # Creates a set [h,e,l,o,w,r,d]
    unique_chars = set(word)

    # len_original = 10, len_set = 7
    len_original = len(cleaned_word)
    len_set = len(unique_chars)

    # len_original (10) > len_set (7)?
    if len_original > len_set:
        return False
    else:
        return True



# TEST ____________________________________________________________________________________

str1 = "Hello World"    # False
str2 = "Complexity"     # True

str3 = "Hi111"          # False
str4 = "Hi123"          # True

print(isUnique(str1))
print(isUnique(str2))
print(isUnique(str3))
print(isUnique(str4))



'''
@ Exercise:     
  1.1 (90p)

@ Description:  
  Is Unique: Implement an algorithm to determine if a string has all unique characters.
  What if you cannot use additional data structures?

@ Questions:
  * The string is an ASCII or a Unicode string?
    Character encodings (standards) to represent characters in binary. 
    The difference is the way they encode and the number of bits that each character use.
    - Unicode: 32-bit, 16-bit and 8-bit (is standardized and supports more languages)
    - ASCII: 8-bits (No accent marks (á) and umlaut (ü), no primes (~)(')(¸)(´))

@ What I want to do?
  * I want to clean the word, making all lower cases, eliminate spaces.
'''