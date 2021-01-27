'''
Maximum Subarray

@ What I have to do?
  Find the contiguous subarray with the maximum sum...

  What is a Contiguous Subarray?
  Could be a single number [1], a pair [1,-3] or even the whole array [1, -3, 2, 1, -1],
  but e.g. [-3,1] can't be a contiguous subarray because it is not contiguous.

@ How I am going to do it?
  
  Kadane's Algorithm
  Is the famous solution, and also the most optimum because is O(n).
  Explanation: https://www.youtube.com/watch?v=58yMrWfUS7k

'''


def maxSubArray(nums):
    
    total_sum = nums[0]  # -2
    max_sum = nums[0]  # -2

    for i in nums[1:]:
        total_sum = max(total_sum + i, i)  # -2+1 = -1   or    1
        max_sum = max(total_sum, max_sum)  #         1   or    -2

    return max_sum



# TEST ____________________________________________________________________________________

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))


# Input:        nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output:       6

# Explanation:  [4,-1,2,1] has the largest sum = 6.
