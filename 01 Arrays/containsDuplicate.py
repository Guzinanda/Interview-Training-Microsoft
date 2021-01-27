'''
Constains Duplicates

@ What I have to do?
  Given an array of integers, find if the array contains any duplicates.
  Return 'True' if any value appears at least twice in the array, and it 
  should return 'False' if every element is distinct.

@ How I am going to do it?

  Set() keeps just unique values.

  01. I want to len(nums) to know how many character the original string has:
      nums = [1,1,2,3]
      compare1 = len(nums)
      compare1 = 4

  02. I will create a set() with its individual characters, and get its len():
      compare2 = set(nums)
      compare2 = len([1,2,3])
      compare2 = 3

  03. If I compare the len() of bowth list and they dont have the same amount 
      of characters, then nums has duplicates.
'''


def containsDuplicate(nums):

    compare1 = len(nums)
    compare2 = len(set(nums))

    if compare1 == compare2:
        return False
    
    else:
        return True



# TEST ______________________________________________________________________________

nums1 = [1,2,3,1]               #* True
nums2 = [1,2,3,4]               #* False
nums3 = [1,1,1,3,3,4,3,2,4,2]   #* True

print(containsDuplicate(nums1))
print(containsDuplicate(nums2))
print(containsDuplicate(nums3))
