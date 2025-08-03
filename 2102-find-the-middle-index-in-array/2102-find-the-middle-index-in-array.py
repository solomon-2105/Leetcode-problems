class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        brr=sum(nums)
        presum=0
        for i in range(len(nums)):
            if presum==brr-presum-nums[i]:
                return i
            presum+=nums[i]
        return -1