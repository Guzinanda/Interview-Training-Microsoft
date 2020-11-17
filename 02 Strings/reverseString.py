'''
Reverse String

@   What I have to do?
    Write a function that reverses a string. 
    The input string is given as an array of characters char[].

@   Example:
    Input: ["h","e","l","l","o"] 
    Output: ["o","l","l","e","h"]

@   How I am going to do it?

    01. I want to iterate the array from the bottom to the head.
    02. Appending the num in place to the end of the array.
    03. Then del from s[0:len(s)]
    04. ''.join() the word to print an string.
'''


def reverseString(s):
    
    i = len(s) - 1  # 4
    initials = len(s)  # 5

    # s = ['h','e','l','l','o','o','l','l','e','h']
    while i >= 0:
        s.append(s[i])
        i -= 1

    # s = ['o','l','l','e','h']
    del s[0:initials]

    # s = "olleh"
    s = ''.join(s)

    return s



# TEST ____________________________________________________________________________________

string1 = ['h','e','l','l','o']     # ['o','l','l','e','h']
print(reverseString(string1))

# Easy one:
string2 = "hello"
print(string2[::-1])
