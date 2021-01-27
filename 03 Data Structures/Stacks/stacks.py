
class Stack():

    def __init__(self):
        self.items = []

    # Push items into the Stack
    def push(self, item):
        self.items.append(item)

    # Pops items out of the Stack
    def pop(self):
        return self.items.pop()

    # Returns what is in the Stack
    def get_stack(self):
        return self.items
    
    # Returns a bool if the Stack is empty or not
    def is_empty(self):
        return self.items == []

    # Return the last item in the Stack if not empty.
    def peek(self):
        if not self.is_empty():
            return self.items[-1]


# TEST __________________________________________________________________________________________

"""
s = Stack()             # Create Stack obj.

s.push('A')            # Push 'A' into the Stack.
s.push('B')            # Push 'B' into the Stack.

print(s.get_stack())    # Return what is in the Stack: 'A' and 'B'.

s.pop()                 # Pops the element in top of the Stack: 'B'.

print(s.get_stack())    # Return what is in the Stack: 'A'.

print(s.is_empty())     # Returns a bool if the Stack is empty or not: False

print(s.peek())         # Return the last item in the Stack if not empty: 'A'
"""
