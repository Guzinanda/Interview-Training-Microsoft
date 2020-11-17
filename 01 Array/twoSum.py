'''
Two Sum

@  What I have to do?
   Given an array of integers 'nums' and an integer 'target', return indices 
   of the two numbers such that they add up to target.

@  How I am going to do it?
'''


def twoSum(nums, target):
    
    #nums = [2,7,11,15]
    #target = 9

    #d= {2:0} 
    d = {}
    
    #   1  7
    for i, num in enumerate(nums):

        #   9        7
        if (target - num) in d:
            #        9        7     1
            return d[target - num], i
        
        d[num] = i



# TEST ____________________________________________________________________________________

nums1 = [2,7,11,15]
target1 = 9
print(twoSum(nums1, target1)) # Output: [0, 1]

nums2 = [3,2,4]
target2 = 6
print(twoSum(nums2, target2)) # Output: [1, 2]

nums3 = [3,3]
target3 = 6
print(twoSum(nums3, target3)) # Output: [0, 1]
