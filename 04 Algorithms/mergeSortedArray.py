"""
@   Merge Sorted Arrays

@   Problem:
    Given two sorted integer arrays nums1 and nums2, merge nums2 the n 
    number of nums into m number of nums1 as one sorted array.

    The number of elements initialized in nums1 and nums2 are m and n 
    respectively. You may assume that nums1 has a size equal to m + n 
    such that it has enough space to hold additional elements from nums2.

@   Template:
 
"""

def merge(nums1, m, nums2, n):

    # Make a copy of the first m elements of nums1.
    nums1_copy = nums1[:m] 
    
    # Read pointers for nums1_copy and nums2 respectively.
    p1 = 0
    p2 = 0
    

     # Compare elements from nums1_copy and nums2 and write the smallest to nums1.
     # We also need to ensure that p1 and p2 aren't over the boundaries of their respective arrays.

    for p in range(n + m):  # range(6) = [0,1,2,3,4,5]
        
        if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
            nums1[p] = nums1_copy[p1] 
            p1 += 1
        else:
            nums1[p] = nums2[p2]
            p2 += 1
    
    return nums1

# TEST ____________________________________________________________________________________

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3

print(merge(nums1, m, nums2, n))
