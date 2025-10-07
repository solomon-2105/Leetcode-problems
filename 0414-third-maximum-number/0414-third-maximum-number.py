class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        fmax,smax,tmax=float('-inf'),float('-inf'),float('-inf')
        for i in nums:
            if i==fmax or i==tmax or i==smax: continue
            if i>fmax:
                tmax=smax
                smax=fmax
                fmax=i
            elif i>smax and i<fmax:
                tmax=smax
                smax=i
            elif i>tmax:
                tmax=i
        return tmax if tmax!=float('-inf') else fmax