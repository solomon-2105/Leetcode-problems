class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a = b = r = nums[0]
        for x in nums[1:]:
            a, b = max(x, a*x, b*x), min(x, a*x, b*x)
            r = max(r, a)
        return r
