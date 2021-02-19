'''
Is Unique

@   Problem
    Implement an algorithm to determine if a string has all unique characters.
    What if you cannot use additional data structures?

@   Template
    The string is an ASCII or a Unicode string?
    Character encodings (standards) to represent characters in binary. 
    The difference is the way they encode and the number of bits that each character use.
     - Unicode: 32-bit, 16-bit and 8-bit (is standardized and supports more languages)
     - ASCII: 8-bits (No accent marks (á) and umlaut (ü), no primes (~)(')(¸)(´))

'''

def cleanString(st):
#* Cleans "st" by make it lowercase and eliminating blank spaces
    st = st.lower()
    st = st.replace(" ", "")
    return st

def isUnique(st):
    word = cleanString(st)
    compared = []
    
    for character in word:
        if character not in compared:
            compared.append(character)
        else:
            return False
    return True



# TEST ____________________________________________________________________________________

st1 = "Hello"           #!... False
st2 = "Love"            #!... True
st3 = "Think Pad"       #!... True

print(isUnique(st1))
print(isUnique(st2))
print(isUnique(st3))
