
def maxSubArray(nums):
    
    total_sum = nums[0]
    max_sum = nums[0]

    for i in nums[1:]:
        total_sum = max(i, total_sum + i)
        max_sum = max(max_sum, total_sum)

    return max_sum



#! TEST __________________________________________________________________________________

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(maxSubArray(nums))



# NOTES __________________________________________________________________________________

# What is a Contiguous Subarray?
# Could be a single number [1], a pair [1,-3] or even the whole array [1, -3, 2, 1, -1],
# but e.g. [-3,1] can't be a contiguous subarray because it is not contiguous.

# What is the problem?
# "Find the contiguous subarray with the maximum sum"

# Bute Force Solution:
# Checking all the possible subarrays and picking the one with the maximum sum.
# It is a possible solution, but it takes a O(n^2) time.

# Optimal Solution:
# Kadane's Algorithm is the famous solution, and also the most optimum because is O(n).
# Explanation: https://www.youtube.com/watch?v=58yMrWfUS7k
