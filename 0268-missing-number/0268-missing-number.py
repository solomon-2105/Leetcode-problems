class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a=sum(range(0,len(nums)+1))
        b=sum(nums)
        return a-b