'''
Cracking the Codding Interview

1.1     Is Unique: Implement an algorithm to determine if a string has all 
        unique characters. Whats if you cannot use additional data structures.
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
