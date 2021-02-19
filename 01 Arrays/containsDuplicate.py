'''
Constains Duplicates

@   Problem
    Given an array of integers, find if the array contains any duplicates.

@   Example
    Input: [1,2,3,1]
    Output: True
    
'''

def containsDuplicate(nums):
    
    d = {}
    
    for i in nums:
        if i not in d:
            d[i] = 1
        else:
            return True
    return False


# Pythnic Way (Easy Way) ____________________________________________________________

#def containsDuplicate(nums):
#    if len(nums) == len(set(nums)):
#        return False
#    else:
#        return True


# TEST ______________________________________________________________________________

nums1 = [1,2,3,1]                   # True
nums2 = [1,2,3,4]                   # False
nums3 = [1,1,1,3,3,4,3,2,4,2]       # True

print(containsDuplicate(nums1))
print(containsDuplicate(nums2))
print(containsDuplicate(nums3))
