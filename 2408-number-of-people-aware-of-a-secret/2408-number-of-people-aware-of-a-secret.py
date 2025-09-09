class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD=10**9+7
        dp=[-1]*(n+1)
        def solve(day):
            if day==1:
                return 1
            if day<=0:
                return 0
            if dp[day]!=-1:
                return dp[day]
            res=0
            for prev in range(day-forget+1,day-delay+1):
                if prev>0:
                    res=(res+solve(prev))%MOD
            dp[day]=res
            return res
        ans=0
        for day in range(n-forget+1,n+1):
            if day>0:
                ans=(ans+solve(day))%MOD
        return ans
