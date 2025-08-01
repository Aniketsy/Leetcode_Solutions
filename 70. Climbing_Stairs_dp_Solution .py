You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

##################################### Recurrence Solution ####################################

  class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n ==1:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)

##################################### Memoization Solution ##################################

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def climb(n):
            if n == 0 or n == 1:
                return 1
            if n in memo:
                return memo[n]
            memo[n] = climb(n - 1) + climb(n - 2)
            return memo[n]

        return climb(n)

################################### Tabulation Solution ##########################################

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=1:
            return 1
        dp = [0]*(n+1)
        dp[0], dp[1] =1,1

        for i in range(2, n+1):
            dp[i] = dp[i-1] +dp[i-2]
        return dp[n]

