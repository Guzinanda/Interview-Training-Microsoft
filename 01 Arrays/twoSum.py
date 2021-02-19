'''
Two Sum

@   Problem
    Given an array of integers 'nums' and an integer 'target', return indices 
    of the two numbers such that they add up to target.

@   Example:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]

'''
    
def twoSum(nums, target):

    # {11:0, 15:1, 2:2, 7:3}
    d = {}

    # [(0, 2),(1,7),(2,11),(3,15)]
    for i, num in enumerate(nums):
        
        m = target - num
        
        if m in d:
            return [d[m], i]
        else:
            d[num] = i


# TEST ____________________________________________________________________________________

nums1 = [11,15,2,7]
target1 = 9
print(twoSum(nums1, target1)) # Output: [0, 1]

'''
nums2 = [3,2,4]
target2 = 6
print(twoSum(nums2, target2)) # Output: [1, 2]

nums3 = [3,3]
target3 = 6
print(twoSum(nums3, target3)) # Output: [0, 1]
'''