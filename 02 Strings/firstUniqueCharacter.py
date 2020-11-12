def firstUniqueCharacter(s):

    # I want to take the character in place.
    # Pop in to compare if there is another equal character in the word:
    #   If there is no other, return its position (index).
    #   If there is another one, insert it back in its position (index).
    

    word = list(s)
    i = 0
    for character in word:
        word.pop(i)
        if character not in word:
            return i
        else:
            word.insert(i,character)
            i += 1
    return -1




# TEST ____________________________________________________________________________________

s1 = "leetcode"         # 0
s2 = "loveleetcode"     # 2
s3 = "momo"             # -1

print(firstUniqueCharacter(s1))
print(firstUniqueCharacter(s2))
print(firstUniqueCharacter(s3))


'''
@   # 03

@   Instructions:
    Given a string, find the first non-repeating character in it and return its index. 
    If it doesn't exist, return -1.

@   Example 01:
    Input:  s = "leetcode"
    Output: 0

@   Example 02:
    Input:  s = "loveleetcode"
    Output: 2

@   Example 03:
    Input:  s = "momo"
    Output: -1


@   Link:
    https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/
'''