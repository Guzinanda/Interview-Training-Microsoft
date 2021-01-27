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

def maximumDepth(root):
    levels = math.floor(math.log(len(root), 2) + 1)
    return levels


# TEST ____________________________________________________________________________________

root = [3, 9, 20, None, None, 15, 7]

print(maximumDepth(root))
