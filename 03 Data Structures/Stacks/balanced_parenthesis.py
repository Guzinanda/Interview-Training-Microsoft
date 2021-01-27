"""
@   Problem
    Use a Stack to check whether or not a string has 
    balanced usage of parenthesis.

@   Example:
    
    (), ()(), (({[]}))      <- Balanced
    ((), {{{)}], [][]]]     <- Not Balanced

    Balanced Example: {[]}
    Non-Balanced Example: (()
    Non-Balanced Example: ))

@   Template:
    01. When you see an open parenthesis: 
        - Push that into a Stack
    02. When you see a close parenthesis: 
        - Peek the las element, if is the open ('[') for that close [']'] pop the stack.
        - Peek the las element, if is not the open ('[') for that close [']'] return False.
"""

from stacks import Stack

def match(p1, p2):
    if p1 == '(' and p2 == ')':
        return True
    elif p1 == '{' and p2 == '}':
        return True
    elif p1 == '[' and p2 == ']':
        return True
    else:
        return False


def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not match(top, paren):
                    is_balanced = False
        
        index += 1
    
    if s.is_empty() and is_balanced:
        return True
    else:
        return False

# TEST __________________________________________________________________________________________

print(is_paren_balanced("()"))
print(is_paren_balanced("("))