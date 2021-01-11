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
    
    # TREE TRAVERSAL
    
    # In order:Izquierda -> Yo -> Derecha
    def maxDepth(self, root):
        def inOrder(root):
            if root == None:
                return
            inOrder(root.left)
            print(root.val)
            inOrder(root.right)
        inOrder(root)
        
        print("\n")
        
    # Pre Order:Izquierda -> Derecha -> Yo
        def preOrder(root):
            if root == None:
                return
            preOrder(root.left)
            preOrder(root.right)
            print(root.val)
        preOrder(root)
        
        print("\n")
            
    # Post Order: Yo -> Izquierda -> Derecha
        def postOrder(root):
            if root == None:
                return
            print(root.val)
            postOrder(root.left)
            postOrder(root.right)
        postOrder(root)
