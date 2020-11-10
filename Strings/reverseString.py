def reverseString(s):
    
    i = len(s) - 1
    initials = len(s)

    while i >= 0:
        s.append(s[i])
        i -= 1

    del s[0:initials]

    return s



#* Test ....................................................................................

string1 = ["h","e","l","l","o"]     #* ["o","l","l","e","h"]
print(reverseString(string1))


# Easy one:
string2 = "hello"
print(string2[::-1])



'''
@   # 01

@   Instructions:
    Write a function that reverses a string. 
    The input string is given as an array of characters char[].

@   Example:
    Input: ["h","e","l","l","o"] 
    Output: ["o","l","l","e","h"]

@   Link:
    https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/
'''
