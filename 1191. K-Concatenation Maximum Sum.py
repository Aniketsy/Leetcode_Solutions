Given an integer array arr and an integer k, modify the array by repeating it k times.

For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2, 1, 2, 1, 2].

Return the maximum sub-array sum in the modified array. Note that the length of the sub-array can be 0 and its sum in that case is 0.

As the answer can be very large, return the answer modulo 109 + 7.

 

Example 1:

Input: arr = [1,2], k = 3
Output: 9
Example 2:

Input: arr = [1,-2,1], k = 5
Output: 2
Example 3:

Input: arr = [-1,-2], k = 7
Output: 0
 

Constraints:

1 <= arr.length <= 105
1 <= k <= 105
-104 <= arr[i] <= 104



###################################################### Solution ##################################################
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = 10**9 + 7

        def kadane(nums):
            max_sum = cur_sum = 0
            for num in nums:
                cur_sum = max(num, cur_sum + num)
                max_sum = max(max_sum, cur_sum)
            return max_sum
        
        max_single = kadane(arr)

        if k == 1:
            return max_single % MOD

        total = sum(arr)
        pre_max = suf_max = cur = 0

        for num in arr:
            cur += num
            pre_max = max(pre_max, cur)

        cur = 0
        for num in reversed(arr):
            cur += num
            suf_max = max(suf_max, cur)

        max_double = pre_max + suf_max

        if total > 0:
            result = max(max_single, max_double + (k - 2) * total)
        else:
            result = max(max_single, max_double)

        return result % MOD

       
