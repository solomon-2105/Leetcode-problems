class Solution:
    def __init__(self):
        self.dp = {}

    def climbStairs(self, n):
        if n <= 2:
            return n
        if n in self.dp:
            return self.dp[n]  # Cached result
        
        # Recursively calculate the number of ways
        self.dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.dp[n]
