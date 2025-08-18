class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD=10**9+7
        count=0
        n=len(s)
        i=0
        while i<n:
            char=s[i]
            length=0
            while i<n and s[i]==char:
                i+=1
                length+=1
            count=count+ (length*(length+1)//2)
            count%=MOD
        return count