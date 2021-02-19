'''
First Missing Positive

@   Problem
    Given an unsorted integer array nums, find the smallest missing positive integer.

@   Example
    Input: nums = [1,2,0]
    Output: 3

    Input: nums = [3,4,-1,1]
    Output: 2

@   Template

    01. Validate if you have nums in your array: if nums:

    02. The smallest positive integer you might find probably will be always in the range of 
        the length of your array, lets say it is an array of 5 numbers, the smallest positive
        integer of those numbes will be always between 1 to 5: range(1, n + 2) were n = 5
        [1,2,3,4,5]
        
    03. Iterate each number in that range asking if the number is in nums till you find it.

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

nums1 = [1, 2, 0]         # 3
nums2 = [3, 4, -1, 1]     # 2
nums3 = [7,8,9,11,12]     # 1
nums4 = [1]               # 2
nums5 = [0]               # 1

print(firstMissingPositive(nums1))
print(firstMissingPositive(nums2))
print(firstMissingPositive(nums3))
print(firstMissingPositive(nums4))
print(firstMissingPositive(nums5))
