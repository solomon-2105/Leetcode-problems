class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD=10**9+7
        dp=[[0]*26 for _ in range(t+1)]
        for c in range(26):dp[0][c]=1
        for k in range(1,t+1):
            for c in range(25):dp[k][c]=dp[k-1][c+1]
            dp[k][25]=(dp[k-1][0]+dp[k-1][1])%MOD
        total=0
        for ch in s:
            total=(total+dp[t][ord(ch)-97])%MOD
        return total
