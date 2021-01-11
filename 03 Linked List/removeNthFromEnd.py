'''
@   Remove Nth Node From End of a Linked List

@   Link:
    https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/
 
@   Instructions:
    Given the head of a linked list, remove the nth node from the end of the list, return its head.

@   Example 01:
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
        
        # Delete
        left.next = left.next.next
        return dummy.next
    