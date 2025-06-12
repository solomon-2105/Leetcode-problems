class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        maxdiff=float('-inf')
        for i in range(1,len(nums)):
            maxdiff=max(maxdiff,abs(nums[i]-nums[i-1]))
        maxdiff=max(maxdiff,abs(nums[-1]-nums[0]))
        return maxdiff