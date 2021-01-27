"""

Reverse a String

@   Problem
    Use a Stack dara structure to invert a string.

@   Example
    Input: "Hello"
    Output: "olleH"

"""

from stacks import Stack

def reverse_string(stack, input_str):

    # Loop through the string and push contents
    # character by character onto Stack:

    for i in range(len(input_str)):
        stack.push(input_str[i])

    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()

    return rev_str

# TEST __________________________________________________________________________________________

stack = Stack()
input_str = "Hello"

print(reverse_string(stack, input_str))
