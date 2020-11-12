   
    # I want to move the last item of the list (index[-1]) in front of the list (index[0])
    # This will be repeated "k" times

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
@   # 03

@   Instructions:
    Given an array of integers, find if the array contains any duplicates.
    Return true if any value appears at least twice in the array, and it 
    should return false if every element is distinct.

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

@   Link:
    https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/
'''