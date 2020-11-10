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



#* Test ....................................................................................

nums1 = [2,2,1]                 #* 1
nums2 = [4,1,2,1,2]             #* 4
nums3 = [7,3,7,2,2]             #* 3


print(singleNumber(nums1))
print(singleNumber(nums2))
print(singleNumber(nums3))



'''
@   # 05

@   Instructions:
    Given a non-empty array of integers, every element appears twice except for one. 
    Find that single one.

@   Example:
    Input: [2,2,1]
    Output: 1

@   Link:
    https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/
'''