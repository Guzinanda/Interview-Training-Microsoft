'''
Climbing Stairs

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


@   What I want to do?

'''


def climbStairs(n):

    path = {1:1, 2:2}

    for i in range(3, n + 1): # range(3,6) -> 3,4,5
        path[i] = path[i-1] + path[i-2]
    
    return path[n]



# TEST ______________________________________________________________________________________________________

n = 5
print(climbStairs(n))

# @ Problem:
#   You are climbing a stair case. It takes n steps to reach to the top.
#   Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# @ Example 1:
#   Input: 2 
#   Output: 2

# @ Explanation: There are two ways to climb to the top.
#   1. 1 step + 1 step
#   2. 2 steps
