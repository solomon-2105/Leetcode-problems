import math
class Solution:
    def minEatingSpeed(self,a:List[int],h:int)->int:
        def brr(a:List[int],i:int)->int:
            s=0
            for j in a:
                s+=math.ceil(j/i)
            return s
        grr=0
        for val in a:
            grr=max(grr,val)
        low,high=1,grr
        while low<=high:
            mid=low+(high-low)//2
            req=brr(a,mid)
            if req<=h:
                high=mid-1
            else:
                low=mid+1
        return low
