'''
Logic:

        3
      /   \ 
     9    20 
          / \ 
        15    7


root = [3 , 9 , 20 , null , null , 15 , 7]
        _   ______   ____________________

Levels:     log2(7)     = 2.8
            floor(2.8)  = 2
            2 + 1       = 3

'''
null = None
import math

def maxDepth(root):
    levels = math.floor(math.log(len(root), 2) + 1)
    return levels


#* Test ....................................................................................

root = [3, 9, 20, None, None, 15, 7]

print(maxDepth(root))


#* Info ....................................................................................
'''
@   # 01

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
