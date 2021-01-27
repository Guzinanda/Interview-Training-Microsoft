'''
@   Tree Traversal Theory

@   Example 01:
    Input: [3,9,20,null,null,15,7]

        3
      /   \ 
     9    20 
          / \ 
        15    7

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    
    def maxDepth(self, root):

        # Pre Order Traversal : Izquierda -> Derecha -> Yo
        def preOrder(root):
            if root == None:
                return
            print(root.val)
            preOrder(root.left)
            preOrder(root.right)
        preOrder(root)

        '''
                A
             /     \ 
            B       C
           / \     / \ 
          D   E   F   G
         / \     / \   \ 
        H   I   J   K   L
        
        A,B,D,H,I,E,C,F,J,K,G,L 
        '''

        print("\n")

        # In Order Traversal : Izquierda -> Yo -> Derecha
        def inOrder(root):
            if root == None:
                return
            inOrder(root.left)
            print(root.val)
            inOrder(root.right)
        inOrder(root)

        '''
                11
             /      \ 
            6        15
           / \      /  \ 
          3   8    13   17
         / \      /  \    \ 
        1   5    12   14  19
        
        1,3,5,6,8,11,12,13,14,15,17,19
        With a BST an In Order Traversal will print the values in increasing order!
        '''

        print("\n")

        # Post Order Traversal : Yo -> Izquierda -> Derecha
        def postOrder(root):
            if root == None:
                return
            postOrder(root.left)
            postOrder(root.right)
            print(root.val)
        postOrder(root)

        '''
                11
             /      \ 
            6        15
           / \      /  \ 
          3   8    13   17
         / \      /  \    \ 
        1   5    12   14  19
        
        1,5,3,8,6,12,14,13,19,17,15,11
        '''

        # Level Order Traversal

        '''
        We need to do a BFS
        '''
