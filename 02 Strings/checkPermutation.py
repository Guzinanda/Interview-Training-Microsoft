'''
Given two strings s1 and s2, return true if s2 contains the permutation of s1. 

Notes:  A permutation is a possible order of elements of a set (conjunto), this 
        means that if we have (a,b,c) we can do 6 possible permutations.
        {5,6,7} -> {5,6,7}, {7,5,6}, {6,7,5}, {5,7,6}, {7,6,5}, {6,5,7}


        For this challenge, I am asking to find if "abd" is a permutation of the
        string "cidbaooo". In other words, if "abd" (in any order) is in "cidbaooo". 

        s1 = "abd"
        S2 = "cidbaooo"
                ___

01:     I want first, to ensure the inputs are viable:
        - If my s1 > s2 I can't even try.
        - If my s1 < s2 then there is a possibility.

02:     I want to se how many times each character apears in s1:
        - Make a collections.Counter() of s1 = "dba" -> {a:1, b:1, d:1}

03:     I want to iterate in s2 using a Sliding Window:
        "eidbaooo"   
         ___
          ___
           ___

        - Take the range of characters and create a collections.Counter() of it.
        - Compare if collections.Counter(s1) == collections.Counter(s2[pi:pf])
        
'''

import collections

def checkInclusion(s1,s2):

    # 01: If my s1 > s2 is not even possible to determine:
    if len(s1) > len(s2):
        return False

    # 02: s1 = "dba" -> {a:1, b:1, d:1}
    compare = collections.Counter(s1)

    # 03: {a:1, b:1, d:1} == {e:1, d:1, i:1}
    pi = 0          # 0
    pf = len(s1)    # 3

    for i in range(len(s2) - len(s1) + 1):
        target = collections.Counter(s2[pi:pf])
        if target == compare:
            return True
        elif (target != compare) and (pf == len(s2)):
            return False

        pi += 1
        pf += 1
    
    

# TEST ____________________________________________________________________________________

s1 = "abd"
s2 = "eidbaooo"
print(checkInclusion(s1,s2)) # True

s1 = "abd"
s2 = "eidaaooo"
print(checkInclusion(s1,s2)) # False



