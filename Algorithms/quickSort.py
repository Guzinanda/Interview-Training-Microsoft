'''
@ Quick Sort

@ Problem
  Given an unsorted integer array nums of n elements, write a function to Quick Sort nums.

@ Example
  Input: nums = [10, 5, 2, 3]
  Output: nums = [2, 3, 5, 10]

@ Template
  01. Arrays of just one element are already sorted, so return the array if is just one element.
  02. We need a pivot, for example the first number in the array.
  03. Tow lists, one with all the nums less than the pivor and another with all the greatest nums.
  04. Return the recution of that algorithm in this order less + pivot + grater

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
