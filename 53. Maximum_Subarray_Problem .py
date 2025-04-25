Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104



################################################  Solution ################################
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        lar_sum = float('-inf')
        current_sum = 0
        start = s = end = 0

        for i in range(len(nums)):
            current_sum += nums[i]

            if current_sum > lar_sum:
                lar_sum = current_sum
                start = s
                end = i

            if current_sum < 0:
                current_sum = 0
                s = i+1

        return  lar_sum
