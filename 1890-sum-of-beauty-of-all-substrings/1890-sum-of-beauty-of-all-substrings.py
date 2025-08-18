class Solution:
    def beautySum(self, s: str) -> int:
        count=0
        n=len(s)
        for i in range(n):
            brr={}
            for j in range(i,n):
                brr[s[j]]=brr.get(s[j],0)+1
                values=brr.values()
                maxi=max(values)
                mini=min(values)
                count+=(maxi-mini)
        return count