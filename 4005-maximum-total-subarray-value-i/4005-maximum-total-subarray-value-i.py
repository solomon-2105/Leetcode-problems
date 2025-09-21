class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        a,b=min(nums),max(nums)
        s=b-a
        return s*k