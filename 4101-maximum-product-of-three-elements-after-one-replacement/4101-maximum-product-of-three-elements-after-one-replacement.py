class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a=nums
        fma,sma,tma=float('-inf'),float('-inf'),float('-inf')
        fmi,smi=float('inf'),float('inf')
        for i in nums:
            if i>fma:
                tma=sma
                sma=fma
                fma=i
            elif i>sma:
                tma=sma
                sma=i
            elif i>tma:
                tma=i
            if i<fmi:
                smi=fmi
                fmi=i
            elif i<smi:
                smi=i
        brr=10**5
        p1=fma*sma*tma
        p2=fmi*smi*fma
        g1=max(fma*sma,fmi*smi)*brr
        g2=(fmi*fma)*-1*brr
        return int(max(p1,p2,g1,g2))