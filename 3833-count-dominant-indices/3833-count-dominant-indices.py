class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        tot = sum(nums)
        right = tot
        count = 0
        for i in range(n-1):
            right -= nums[i]
            rc = n - i - 1
            avg = right // rc
            if avg < nums[i]:
                count += 1
        return count