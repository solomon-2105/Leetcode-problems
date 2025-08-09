import math
class Solution:
    def brr(self,a,i):
        s=0
        for j in a:
            s+=math.ceil(j/i)
        return s<=self.t

    def smallestDivisor(self, a: List[int], t: int) -> int:
        l,h=1,max(a)
        self.t=t
        ans=0
        while l<=h:
            m=l+(h-l)//2
            if self.brr(a,m):
                ans=m
                h=m-1
            else:
                l=m+1
        return ans
