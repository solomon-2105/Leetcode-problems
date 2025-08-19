import math
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime:List[int], waterDuration: List[int]) -> int:
        n=len(landStartTime)
        m=len(waterStartTime)
        res=math.inf
        for i in range(n):
            for j in range(m):
                a=landStartTime[i]+landDuration[i]
                b=max(a,waterStartTime[j])
                c=b+waterDuration[j]
                d=waterStartTime[j]+waterDuration[j]
                e=max(d,landStartTime[i])
                f=e+landDuration[i]
                res=min(res,c,f)
        return res