"""
Linked List (Singly Linked List)

        HEAD

NODE   [A  |   ]  ->  [B|]  ->  [C|]  ->  [D|]  ->  NULL
       DATA NEXT

"""

class Node:
    def __init__(self, data):   # Constructor
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):         # Constructor
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next


    # Append new nodes and creates the initial node if there is no one: [A|] -> NULL or [A|] -> [B|] -> NULL
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node        


    # Insert at the beggining of the Linked List: [E|] -> [A|] -> [B|] -> NULL
    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node


    # Insert a node in a place: [A|] -> [B|] -> [E|] -> [C|] -> NULL
    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in the list")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node


    # Delete a node by key (value)
    def delete_node(self,key):
        cur_node = self.head

        # If is the head:
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return
        
        # If is anithing else:
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next
        
        if cur_node is None:
            return

        prev.next = cur_node.next

    
    # Delete a node by position
    def delete_node_at_pos(self, pos):
        cur_node = self.head

        # If is the head:
        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return 

        # If is anything else:
        prev = None
        count = 0
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1
        
        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None
    

    # Know the len of the Linked List in a iterative way
    def len_iterative(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count


    # Know the len of the Linked List in a recursive way
    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)


# TEST __________________________________________________________________________________________

"""
llist = LinkedList()

llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')

llist.prepend('E')

llist.insert_after_node(llist.head.next, "F")

llist.delete_node('B')

llist.delete_node_at_pos(4)

print(llist.len_iterative())
print(llist.len_recursive(llist.head))

llist.print_list()
"""
