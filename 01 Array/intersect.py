'''
Intersection of Two Arrays II

@ What I have to do?
  Compute the intersection of two given arrays.
  They will give me two arrays with numbers, nums1 is the 
  intersector and nums2 is the intersected.


@ How I am going to do it?

  Dictionaries allow me to store information based in a key (reference).

  01. I need to create a Dictionary that indicates me how many nums nums1 have.
      This is done by iterating nums1 to store the data in dict1:
      nums1 = [4,4,9,5]
      dict1 = [4:2, 9:1, 5:1]

  02. I have to compare each num in nums2, if it is in dict1 and it is grater
      than 0, then I can store it in a list and substract that reference from dict1
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



# TEST ______________________________________________________________________________

nums1 = [4,4,9,5]
nums2 = [9,4,9,8,4]

print(intersect(nums1, nums2))