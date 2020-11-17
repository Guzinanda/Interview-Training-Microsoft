'''
Climbing Stairs

@ What I have to do?
  You are climbing a stair case. It takes 'n' steps to reach to the top.
  Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

@ Example:
  Input: 4 
  Output: 5

@ By hand try to figure out a sequence pattern in the outputs of the problem 

  5 Steps -> [1,1,1,1,1]  [1,1,1,2]  [1,1,2,1]  [1,2,1,1]  [2,1,1,1]  [1,2,2]  [2,1,2]  [2,2,1]   -> 8 ways    
  4 Steps -> [1,1,1,1]    [1,1,2]    [1,2,1]    [2,1,1]    [2,2]                                  -> 5 ways    
  3 Steps -> [1,1,1]      [1,2]      [2,1]                                                        -> 3 ways   
  2 Steps -> [1,1]        [2]                                                                     -> 2 ways   
  1 Step  -> [1]                                                                                  -> 1 ways   


@ Fibonacci Sequence:
  If we analice the outcomes we can see the fibonacci pattern: (1) -> (2) -> (1+2 = 3) -> (2+3 = 5) -> (3+5 = 8)
  
  In other words, we know that we start with 1 and 2 (they are always like this), but before that the pattern is 
  to add the previous two numbers in the sequence to know the last number in it...

@ How I am going to do it?

  01. I will create a dictionary with the first two stairs combination, 1:1 and 2:2. 
  02. Because I already know 1:1 and 2:2, I will keep adding the secuence patterns required
      to reach till the number I am looking for, and the new path will be the sum of the number
      two places back and one place back.
  03. I will return the path[n] I an looking for because I already add all the missing ones.
'''


def climbStairs(n):

    path = {1:1, 2:2}

    for i in range(3, n + 1): # range(3,6) -> 3,4,5
        path[i] = path[i-2] + path[i-1]
    
    return path[n]



# TEST ____________________________________________________________________________________

n1 = 5
print(climbStairs(n1))  # 8

n2 = 1
print(climbStairs(n2))  # 1
