'''
@   Maximum Depth of Binary Tree
 
@   Instructions:
    Given a binary tree, find its maximum depth.
    The maximum depth is the number of nodes along the longest path from the root node 
    down to the farthest leaf node. Note: A leaf is a node with no children.

@   Example 01:
    Input: [3,9,20,null,null,15,7]

        3
      /   \ 
     9    20 
          / \ 
        15    7

@   Link:
    https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/555/
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
