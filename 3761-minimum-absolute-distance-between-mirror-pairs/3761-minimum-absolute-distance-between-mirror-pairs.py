class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        brr,grr={},float('inf')
        for i in range(len(nums)):
            if nums[i] in brr:
                grr=min(grr,i-brr[nums[i]])
            frr=int(str(nums[i])[::-1])
            brr[frr]=i
        if grr!=float('inf'): return grr
        return -1