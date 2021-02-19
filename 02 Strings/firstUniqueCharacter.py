'''
First Unique Character

@   Problem
    Given a string, find the first non-repeating character in it and return its index. 
    If it doesn't exist, return -1.

@   Example 01
    Input:  s = "leetcode"
    Output: 0

    Example 02
    Input:  s = "loveleetcode"
    Output: 2

    Example 03
    Input:  s = "momo"
    Output: -1

@   Template
    I want to take the character in place and Pop in to compare:
    - If there is no other, return its position (index).
    - If there is another one, insert it back in its position (index).

'''

def firstUniqueCharacter(s):
    
    # word = ['l','e','e','t','c','o','d','e']
    word = list(s)
    
    i = 0

    for character in word:
        word.pop(i)
        if character not in word:
            return i
        else:
            word.insert(i, character)
            i += 1
    
    return -1



# TEST ____________________________________________________________________________________

s1 = "leetcode"         # 0
s2 = "loveleetcode"     # 2
s3 = "momo"             # -1

print(firstUniqueCharacter(s1))
print(firstUniqueCharacter(s2))
print(firstUniqueCharacter(s3))
