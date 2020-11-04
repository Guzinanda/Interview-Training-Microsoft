
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




#! TEST __________________________________________________

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
