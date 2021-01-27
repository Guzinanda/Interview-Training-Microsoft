'''
A Linked List is a Data Structure for sorting a collection of items.
It does it in a different way from the way an array does it.

An array can be visualized as a long box whit many partitions of the same size:
[6|3|4|2|1]

A linked list can be visualized as many boxes that are connected to each other:
[6]->[3]->[4]->[2]->[1]

'''

class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
    
    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total
    
    def display(self):
        elements = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elements.append(cur_node.data)
            print(elements)
    
    def get(self,index):
        if index >= self.length():
            print("ERROR: 'Get' Index out of range!")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index: 
                return cur_node.data
                cur_idx += 1
    
    def erase(self, index):
        if index >= self.length():
            print("ERROR: 'Erase' Index out of range!")
            return
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx += 1


my_list = linked_list()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.display()


my_list.erase(1)
#my_list.display()
