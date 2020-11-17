'''
Move Zeroes

@ What I have to do?
  Given an array move all 0's to the end mantaining the order of the rest. 

@ How I am going to do it?
  01. Iterate the array from index[initial] to index[final]
  02. If I found a 0 substitute if for a '*' and append a '0' to the end.
  03. Remove() all '*'
'''


def moveZeroes(nums):

    for i in range(len(nums)):
        if nums[i] == 0:
            nums[i] = '*'
            nums.append(0)

    while (nums.count('*')):
        nums.remove('*')

    return nums



# TEST ______________________________________________________________________________

nums1 = [0,1,0,3,12]  #[1,3,12,0,0]
print(moveZeroes(nums1))
