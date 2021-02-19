'''
Rotate an Array

@   Problem
    Given an array of integers, and a 'k' number indicating the number of times
    the arrays must be rotated, totate that number to the right.

@   Example
    Input:  nums = [1,2,3,4,5,6,7], k = 3
    Output: [5,6,7,1,2,3,4]

@   Template
    I want to move the last item of the list (index[-1]) in front of the list (index[0])
    This will be repeated "k" times

'''

def rotateArray(nums, k):
    while k > 0:
        last_item = nums.pop(-1)
        nums.insert(0, last_item)
        k -= 1

    return nums


# TEST ____________________________________________________________________________________

nums1 = [1,2,3,4,5,6,7]             # [5,6,7,1,2,3,4]
k1 = 3

nums2 = [-1,-100,3,99]              # [3,99,-1,-100]
k2 = 2

print(rotateArray(nums1, k1))
print(rotateArray(nums2, k2))
