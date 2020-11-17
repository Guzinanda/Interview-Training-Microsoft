'''
Single Number

@  What I have to do?
   Given a non-empty array of integers, every element appears twice except one. 
   Find that single one.

   Example:
   Input: [2,2,1]
   Output: 1

@  How I am going to do it?
   
   With dictionaries.

   01. I want to create a dictionary with each time a number repites itself.
   02. I tant to iterate that dictionary for the character with '1'
'''


def singleNumber(nums):

    #numsOccurrences = dict()
    numsOccurrences = {}

    for i in nums:
        if i in numsOccurrences:
            numsOccurrences[i] += 1
        else:
            numsOccurrences[i] = 1

    for i in numsOccurrences:
        if numsOccurrences[i] == 1:

            return i



# TEST ____________________________________________________________________________________

nums1 = [2,2,1]                 #* 1
nums2 = [4,1,2,1,2]             #* 4
nums3 = [7,3,7,2,2]             #* 3


print(singleNumber(nums1))
print(singleNumber(nums2))
print(singleNumber(nums3))
