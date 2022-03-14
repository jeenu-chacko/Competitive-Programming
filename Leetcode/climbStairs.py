class Solution:
    def climbStairs(self, n: int, memo= {0:0, 1:1,2:2}) -> int:
        if n in memo:
            return memo[n]
        
        memo[n] = self.climbStairs(n - 1, memo) + self.climbStairs(n - 2, memo)
        return memo[n]