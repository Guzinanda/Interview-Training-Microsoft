def containsDuplicate(nums):

    compare1 = len(nums)
    compare2 = len(set(nums))

    if compare1 == compare2:
        return False
    
    else:
        return True



#* Test ....................................................................................

nums1 = [1,2,3,1]               #* True
nums2 = [1,2,3,4]               #* False
nums3 = [1,1,1,3,3,4,3,2,4,2]   #* True

print(containsDuplicate(nums1))
print(containsDuplicate(nums2))
print(containsDuplicate(nums3))


'''
@   # 04

@   Instructions:
    Given an array of integers, find if the array contains any duplicates.
    Return true if any value appears at least twice in the array, and it 
    should return false if every element is distinct.

@   Example:
    Input: [1,2,3,1]
    Output: true

@   Link:
    https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/
'''