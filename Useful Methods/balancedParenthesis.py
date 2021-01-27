'''
Valid Parentesis

@  What I have to do?
   Determine if is a valid parentesis.

@  How I am going to do it?

   01. I will create 1 dictionary and 2 arrays:
       - bracket_map  : that is a dictionary with all the types or parentesis.
       - open_bracket : that is an array with just the open parentesis.
       - stack        : that is an empty array.

   02. I will iterate each character user gaves me.
       - If i is in open brackets (witch means that is an open bracket) just stack.append(i)
       - If stack has something and bracket_map[stack[-1]] , then pop the last in stack
       - Else return False because is not valid
   
   03. return stack == [] (if its empty is True)
'''

def isValid(s):
    
    bracket_map = {"(": ")", "[": "]",  "{": "}"}

    open_bracket = ["(", "[", "{"]

    stack = []

    for i in s:
        if i in open_bracket:
            stack.append(i)
        elif stack and i == bracket_map[stack[-1]]:
                stack.pop()
        else:
            return False

    return stack == []



# TEST ____________________________________________________________________________________

# Example 01:
#s1 = "()"        
#print(isValid(s1))  # Output:   True

# Example 02:
#s2 = "()[]{}"    
#print(isValid(s2))  # Output:   True

# Example 03:
#s3 = "(]"
#print(isValid(s3))  # Output:   False

# Example 04:
#s4 = "([)]"
#print(isValid(s4))  # Output:   False

# Example 05:
#s5 = "{[]}"
#print(isValid(s5))  # Output:   True

# Example 06:
s6 = "([]{})"
print(isValid(s6))  # Output:   True
