# Logic ....................................................................................

# 1. Create list where I am going to be putting my numbers (mergeArray)
# 2. Iterate nums1 appending the first m numbers to the list mergeArray

# 3. Iterate nums2



def merge(nums1, m, nums2, n):

    mergedArray = []

    for i in range(m):
        mergedArray.append(nums1[i])

    for i in range(n):
        mergedArray.append(nums2[i])

    return sorted(mergedArray)


# Tests ....................................................................................

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3

print(merge(nums1, m, nums2, n))



'''
@   # 01

@   Instructions:
    Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

@   Example 01:
    Input:  nums1 = [1,2,3,0,0,0], m = 3
            nums2 = [2,5,6],       n = 3

    Output: [1,2,2,3,5,6]

@   Link:
    https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/555/
'''