'''
@ First Missing Positive

@ Problem Link:
  https://leetcode.com/problems/first-missing-positive/

@ Problem
  Given an unsorted integer array nums, find the smallest missing positive integer.

@ Example
  Input: nums = [1,2,0]
  Output: 3

  Input: nums = [3,4,-1,1]
  Output: 2

@ Template

'''

def firstMissingPositive(nums):

    if nums:
        n = len(nums) # 1
        n = range(1, n + 2) # 1, 2

        for i in n:
            if i not in nums:
                return i
    else:
        return 1
        

    # TEST ____________________________________________________________________________________________

nums1 = [1, 2, 0] 
print(firstMissingPositive(nums1)) # 3

nums2 = [3, 4, -1, 1]
print(firstMissingPositive(nums2)) # 2

nums3 = [7,8,9,11,12]
print(firstMissingPositive(nums3)) # 1

nums4 = [1]
print(firstMissingPositive(nums4)) # 2

nums5 = [0]
print(firstMissingPositive(nums5)) # 1
