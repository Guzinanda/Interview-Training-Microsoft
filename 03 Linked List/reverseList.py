'''
@   Reverse Linked List

@   Link:
    https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/560/
 
@   Instructions:
    Reverse a singly linked list.

@   Example 01:
    Input:  1 -> 2 -> 3 -> 4 -> 5 -> NULL
    Output: 5 -> 4 -> 3 -> 2 -> 1 -> NULL
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev