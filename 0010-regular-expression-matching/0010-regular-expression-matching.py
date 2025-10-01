class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        a=len(s)
        b=len(p)
        dp=[[False]*(b+1) for _ in range(a+1)]
        dp[0][0]=True
        for j in range(1,b+1):
            if p[j-1]=="*":
                dp[0][j]=dp[0][j-2]
        for i in range(1,a+1):
            for j in range(1,b+1):
                c={s[i-1],'.'}
                if p[j-1] in c:
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=="*":
                    dp[i][j]=dp[i][j-2]
                    if p[j-2] in c:
                        dp[i][j]=dp[i][j] or dp[i-1][j]
        return dp[a][b]