class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        fmax,smax,tmax=float('-inf'),float('-inf'),float('-inf')
        for i in nums:
            if i>fmax:
                tmax=smax
                smax=fmax
                fmax=i
            elif i>smax and i<fmax:
                tmax=smax
                smax=i
            else:
                tmax=i
        return fmax if tmax==float('-inf') else tmax