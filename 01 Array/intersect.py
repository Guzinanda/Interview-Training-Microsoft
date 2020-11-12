'''
Intersection of Two Arrays II

@ What I have to do?
  Compute the intersection of two given arrays.

@ Who I am going to do it?

'''

def intersect(nums1, nums2):
    
    dict1 = dict()
    
    # i = [4,4,9,5]
    # dict1 = [4:2,9:1,5:1]
    for i in nums1:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] += 1
    

    ret = []
    
    # i = [9,4,9,8,4]
    # ret = [9,4,4]
    for i in nums2:
        if i in dict1 and dict1[i]>0:
            ret.append(i)
            dict1[i] -= 1
    
    return ret


# TEST ____________________________________________________________________________________

nums1 = [4,4,9,5]
nums2 = [9,4,9,8,4]

print(intersect(nums1, nums2))