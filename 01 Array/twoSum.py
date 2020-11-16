
def twoSum(nums, target):
    
    d = {}
    
    for i, num in enumerate(nums):
        
        if target-num in d:
            return d[target-num], i
        
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
