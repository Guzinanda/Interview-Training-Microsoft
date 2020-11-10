def removeDuplicates(nums):

    i = 0
    while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            del nums[i]
        else:
            i += 1
    return len(nums)




#* Test ....................................................................................

nums1 = [1,1,2]                 #* [1,2]
nums2 = [0,0,1,1,1,2,2,3,3,4]   #* [0,1,2,3,4]

print(removeDuplicates(nums1))
print(removeDuplicates(nums2))


'''
@   # 01

@   Instructions:
    Remove Duplicates from Sorted Array
    Given a sorted array nums, remove the duplicates in-place such that each element appear 
    only once and return the new length. Do not allocate extra space for another array, you 
    must do this by modifying the input array in-place with O(1) extra memory.

@   Example:
    Given nums = [0,0,1,1,1,2,2,3,3,4],
    Your function should return length = 5, 

@   Link:
    https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
'''