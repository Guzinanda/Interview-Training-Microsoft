'''
@ Quick Sort

@ Problem
  Given an unsorted integer array nums of n elements, write a function to Quick Sort nums.

@ Example 01:
  Input: nums = [10, 5, 2, 3]
  Output: nums = [2, 3, 5, 10]

@ Notes

'''


def quickSort(array):

    if len(array) < 2:
        return array

    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        return quickSort(less) + [pivot] + quickSort(greater)


# TEST ____________________________________________________________________________________________

nums1 = [10, 5, 2, 3]
print(quickSort(nums1))

nums2 = [2,0,2,1,1,0]
print(quickSort(nums2))
