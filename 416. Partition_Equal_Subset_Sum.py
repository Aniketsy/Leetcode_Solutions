Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 
Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100

####################### Solution  ##################
class Solution:
  def canPartition(self, nums: list[int]) -> bool:
    summ = sum(nums)
    if summ % 2 == 1:
      return False
    return self.knapsack_(nums, summ // 2)

  def knapsack_(self, nums: list[int], subsetSum: int) -> bool: 
    dp = [False] * (subsetSum + 1)
    dp[0] = True

    for num in nums:
      for i in range(subsetSum, num - 1, -1):
        dp[i] = dp[i] or dp[i - num]

    return dp[subsetSum]
