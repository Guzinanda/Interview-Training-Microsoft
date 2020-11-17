'''
Rotate an Array

@  What I have to do?
   Given an array of integers, and a 'k' number indicating the number of times
   the arrays must be rotated, totate that number to the right.

@  How I am going to do it?
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

nums1 = [1,2,3,4,5,6,7]
k1 = 3

nums2 = [-1,-100,3,99]
k2 = 2

print(rotateArray(nums1, k1))
print(rotateArray(nums2, k2))


'''
@   Example 01:
    Input:  nums = [1,2,3,4,5,6,7], k = 3
    Output: [5,6,7,1,2,3,4]
    
    Explanation:
    rotate 1 steps to the right: [7,1,2,3,4,5,6]
    rotate 2 steps to the right: [6,7,1,2,3,4,5]
    rotate 3 steps to the right: [5,6,7,1,2,3,4]

@   Example 02:
    Input:  nums = [-1,-100,3,99], k = 2
    Output: [3, 99,-1,-100]
    
    Explanation:
    rotate 1 steps to the right: [7,1,2,3,4,5,6]
    rotate 2 steps to the right: [6,7,1,2,3,4,5]
    rotate 3 steps to the right: [5,6,7,1,2,3,4]
'''
