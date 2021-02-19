'''
@   Problem
    Given a sorted (in ascending order) integer array nums of n elements and a target value, write 
    a function to search target in nums. If target exists, then return its index, otherwise return -1.

@   Theory
    Binary Search should be considered every time you need to search for a index in a collection that 
    is sorted (if not we can always sort it first befor applying Binary Search).

    Pre-Processing: Sort if collection is unsorted.
    Binary Search: Use a loop or recursion to divide the search space in half each comparasion.
    Post-Processing: Determine viable candidates remaning space.

@   Template

'''

def binarySearch(list, item):

    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None

    
# TEST ____________________________________________________________________________________

print("Example 01")
list1 = [-1,0,3,5,9,12]
item1 = 9
print(binarySearch(list1, item1))

print("Example 02")
list2 = [-1,0,3,5,9,12]
item2 = 2
print(binarySearch(list2, item2))
